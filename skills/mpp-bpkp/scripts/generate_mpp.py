"""Isi paket DOCX asli tanpa membangun ulang kop/tabel. Preflight sebelum publikasi."""
import argparse
from copy import deepcopy
from datetime import date, datetime, timedelta
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E
import openpyxl
from schema import ROOT, VERSION, TEMPLATE_IDENTITY, PROFILE_FIELDS
from office_io import recalculate_xlsx, render_documents

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}; Q=lambda s:'{'+W+'}'+s
TOKEN=re.compile(r'\{\{([A-Z0-9_]+)\}\}')
MONTHS=['','Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

from model import InputError, fmt, nonempty, lines, read_model, words

def text(el):return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def tokens(root,mapping):
    """Replace even if Word split a placeholder over multiple runs; keep run styles."""
    for p in root.xpath('//w:p',namespaces=NS):
        nodes=p.xpath('.//w:t',namespaces=NS);original=''.join(n.text or '' for n in nodes)
        for match in reversed(list(TOKEN.finditer(original))):
            value=fmt(mapping.get(match[1],''));start,end=match.span();pos=0;touched=[]
            for n in nodes:
                count=len(n.text or '')
                if pos<end and pos+count>start:touched.append((n,pos))
                pos+=count
            if not touched:continue
            first,offset=touched[0];last,lastpos=touched[-1]
            prefix=(first.text or '')[:start-offset];suffix=(last.text or '')[end-lastpos:]
            first.text=prefix+value+(suffix if first is last else '')
            first.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
            for n,_ in touched[1:]:n.text=''
            if first is not last:last.text=suffix

def set_cell(cell,value):
    old=cell.find(Q('p'));prototype=deepcopy(old) if old is not None else E.Element(Q('p'))
    for p in list(cell):
        if p.tag!=Q('tcPr'):cell.remove(p)
    for line in str(value if value is not None else '').split('\n'):
        p=deepcopy(prototype);rpr=p.find('.//'+Q('rPr'))
        for child in list(p):
            if child.tag!=Q('pPr'):p.remove(child)
        r=E.SubElement(p,Q('r'))
        if rpr is not None:r.append(deepcopy(rpr))
        t=E.SubElement(r,Q('t'));t.text=line;t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');cell.append(p)

def rows_replace(table,values,header=1,prototype_index=None):
    rows=table.findall(Q('tr'));proto=deepcopy(rows[prototype_index if prototype_index is not None else header])
    for r in rows[header:]:table.remove(r)
    for values_row in values:
        r=deepcopy(proto)
        for c,value in zip(r.findall(Q('tc')),values_row):set_cell(c,fmt(value))
        table.append(r)

def body_tables(root):return root.xpath('/w:document/w:body/w:tbl',namespaces=NS)
def repeat_paragraphs(root,pattern,values):
    ps=[p for p in root.xpath('/w:document/w:body/w:p',namespaces=NS) if re.search(pattern,text(p))]
    if not ps:return
    parent=ps[0].getparent();idx=parent.index(ps[0]);proto=deepcopy(ps[0])
    sections=[deepcopy(s) for p in ps for s in p.xpath('./w:pPr/w:sectPr',namespaces=NS)]
    for s in proto.xpath('./w:pPr/w:sectPr',namespaces=NS):s.getparent().remove(s)
    for p in ps:parent.remove(p)
    key=TOKEN.search(text(proto))[1]
    inserted=[]
    for i,v in enumerate(values):
        p=deepcopy(proto);tokens(p,{key:v});parent.insert(idx+i,p)
        inserted.append(p)
    if sections:
        if not inserted:inserted=[E.Element(Q('p'))];parent.insert(idx,inserted[0])
        properties=inserted[-1].find(Q('pPr'))
        if properties is None:properties=E.Element(Q('pPr'));inserted[-1].insert(0,properties)
        properties.append(sections[-1])

def collapse_section(root,trim=False):
    body=root.find(Q('body'));breaks=[p for p in body.findall(Q('p')) if p.find('./'+Q('pPr')+'/'+Q('sectPr')) is not None]
    if not breaks:return
    p=breaks[0];properties=deepcopy(p.find('./'+Q('pPr')+'/'+Q('sectPr')));i=body.index(p)
    if trim:
        for el in list(body)[i:]:
            if el.tag!=Q('sectPr'):body.remove(el)
    else:body.remove(p)
    old=body.find(Q('sectPr'))
    if old is not None:body.replace(old,properties)

def values_for(model):
    data=model['data'];v={k:fmt(x) for k,x in data.items()};v.update({k:fmt(x) for k,x in model['narratives'].items()});v.update({k:fmt(x) for k,x in model['pia'].items()})
    v.update({'TUJUAN_1':v['TUJUAN_PENGAWASAN'],'DASAR_PENUGASAN':v['DASAR_HUKUM_RINGKAS'],'HAL_SURAT_PENGANTAR':v['HAL_SURAT_PENGANTAR'] or v['NAMA_PENUGASAN'],'JUMLAH_LAMPIRAN_TERBILANG':'Satu surat tugas','HARI_TERBILANG':words(data['JUMLAH_HARI']),'RMP':v['PERS_MULAI'],'PERIODE_UJI':v['LAKS_MULAI']+' sampai dengan '+v['LAKS_SELESAI'],'JUMLAH_PM':'1','JUMLAH_PT':'1','JUMLAH_KT':'1','JUMLAH_AT':str(len(model['team'])-3),'RUANG_TTD_ATAU_TTE':''})
    for suffix,person in zip(['KORWAS','DALNIS','KT'],model['team'][:3]):v['NAMA_'+suffix]=person['name'];v['NIP_'+suffix]=person['nip']
    for i,p in enumerate(model['team'],1):v.update({f'NAMA_{i}':p['name'],f'NIP_{i}':p['nip'],f'G{i}':p['gol'],f'JAM_{i}':fmt(sum(p['hours'])),f'REAL_{i}':''})
    for i in range(3):
        for role,ps in [('PM',model['team'][:1]),('PT',model['team'][1:2]),('KT',model['team'][2:3]),('AT',model['team'][3:])]:v[f'{role}{i+1}']=fmt(sum(p['hours'][i] for p in ps))
        v[f'JML{i+1}']=fmt(model['stages'][i]);v[f'PEKERJAAN_{i+1}']=['Persiapan','Pelaksanaan','Penyelesaian'][i]
    for role in ['PM','PT','KT','AT']:v[role+'T']=fmt(sum(float(v[f'{role}{i}'].replace(',','.')) for i in [1,2,3]))
    v['JMT']=fmt(sum(model['stages']))
    v.update({'JP':fmt(model['stages'][0]),'JS':fmt(model['simpulan']),'JK':fmt(model['final_kk']),'JL':fmt(model['stages'][2]-model['final_kk']),'JT':v['JMT'],'KS':''})
    for key,source in [('TGL_RAPAT','PERS_MULAI'),('TGL_TELAAH','PERS_MULAI'),('TGL_ANALISIS','PERS_SELESAI'),('TGL_DOKUMENTASI','PERS_SELESAI'),('TGL_PROSEDUR_LAIN','PERS_SELESAI'),('TGL_ENTRY','LAKS_MULAI'),('TGL_EXIT','SELESAI_MULAI'),('TGL_FINAL_KK','SELESAI_AKHIR'),('TGL_KIRIM_LAPORAN','RPL')]:v[key]=v[source]
    return v

def adapt_document(root,num,m,v):
    ts=body_tables(root);team=m['team'];full=[[i,p['name'],p['nip'],p['role']] for i,p in enumerate(team,1)]
    if num==1:rows_replace(ts[2],[[p['role'],p['name']] for p in team],0)
    if num==2:
        rs=ts[0].findall(Q('tr'))
        for idx,r in enumerate(rs):
            if idx in range(2,6):status='N/A' if m['jenis']=='PIA' else fmt(m['data'].get('STATUS_CEK_PIA') or 'TERSEDIA')
            elif idx in range(6,14):status=fmt(m['data'].get('STATUS_CEK_DPP') or 'TERSEDIA')
            elif idx==15:status=fmt(m['data'].get('STATUS_CEK_RENCANA') or 'TERSEDIA')
            elif idx==16:status=fmt(m['data'].get('STATUS_CEK_KM6') or 'TERSEDIA')
            else:continue
            set_cell(r.findall(Q('tc'))[-1],{'TERSEDIA':'✓','BELUM':'','N/A':'N/A'}.get(status.upper(),''))
    if num==3:rows_replace(ts[3],[[i,p['name'],p['nip'],p['gol'],p['role']] for i,p in enumerate(team,1)])
    if num==4:
        rows_replace(ts[1],[[p['role'],':',p['name']] for p in team],0)
        repeat_paragraphs(root,r'\{\{IHP_\d+\}\}',[r[0] for r in m['tables']['IHP']])
        repeat_paragraphs(root,r'\{\{TUJUAN_[123]\}\}',[v[k] for k in ['TUJUAN_1','TUJUAN_2','TUJUAN_3'] if v.get(k)])
    if num==5:
        tembusan=[r[0] for r in m['tables']['TEMBUSAN']]
        if tembusan:repeat_paragraphs(root,r'\{\{TEMBUSAN_\d+\}\}',tembusan)
        else:
            for p in root.xpath('/w:document/w:body/w:p',namespaces=NS):
                if text(p) in ['Tembusan Yth.:','Daftar terlampir']:p.getparent().remove(p)
            collapse_section(root,trim=True)
    if num==6:rows_replace(ts[0],full)
    if num==8:rows_replace(ts[3],[[('Pengendali Mutu' if i==0 else p['role'])+': '+p['name'],fmt(sum(p['hours'])),''] for i,p in enumerate(team)])
    if num==9:
        # Optional result rows must disappear instead of producing empty numbered data.
        inds=[[i,v.get(f'INDIKATOR_PIA_{i}',''),v.get(f'NILAI_PIA_{i}',''),v.get(f'SUMBER_PIA_{i}','')] for i in range(1,5) if v.get(f'INDIKATOR_PIA_{i}')]
        risks=[[i,v.get(f'ISU_PIA_{i}',''),v.get(f'BUKTI_PIA_{i}',''),v.get(f'USUL_PIA_{i}','')] for i in range(1,4) if v.get(f'ISU_PIA_{i}')]
        rows_replace(ts[1],inds or [['','Tidak disajikan dalam tabel; lihat uraian hasil PIA.','','']]);rows_replace(ts[2],risks or [['','Lihat uraian hasil PIA dan usulan tindak lanjut.','','']])
        for pattern in [r'\{\{DASAR_PIA_\d+\}\}',r'\{\{METODE_PIA_\d+\}\}']:
            ps=[p for p in root.xpath('/w:document/w:body/w:p',namespaces=NS) if re.search(pattern,text(p))]
            for p in ps:
                key=TOKEN.search(text(p))[1]
                if not v.get(key):p.getparent().remove(p)
    if num==10:
        repeat_paragraphs(root,r'\{\{IHP_\d+\}\}',[r[0] for r in m['tables']['IHP']])
        body=root.find(Q('body'))
        goal=next((p for p in body.findall(Q('p')) if text(p)=='{{TUJUAN_PENGAWASAN}}'),None)
        if goal is not None:
            end_section=goal.find('./'+Q('pPr')+'/'+Q('sectPr'))
            if end_section is not None:end_section.getparent().remove(end_section)
            position=body.index(goal)+1
            last_goal_paragraph=goal
            for objective in m['plan']['objectives']:
                source=objective['source'];label=objective['id']
                label+= ' [usulan tentatif]' if source['kind']=='USULAN_TENTATIF' else ' [pedoman pusat]'
                origin=('Dasar usulan: '+source['basis']) if source['kind']=='USULAN_TENTATIF' else ('Sumber: '+Path(source['path']).name+', '+source['location'])
                dummy=E.Element(Q('tc'));dummy.append(deepcopy(goal));set_cell(dummy,label+': '+objective['text']+'\n'+origin)
                for paragraph in list(dummy):body.insert(position,paragraph);position+=1;last_goal_paragraph=paragraph
            if end_section is not None:
                properties=last_goal_paragraph.find(Q('pPr'))
                if properties is None:properties=E.Element(Q('pPr'));last_goal_paragraph.insert(0,properties)
                properties.append(end_section)
        body=root.find(Q('body'));ps=list(body);a=next(i for i,p in enumerate(ps) if text(p)=='Metodologi pengawasan dilaksanakan melalui:');b=next(i for i,p in enumerate(ps[a+1:],a+1) if text(p)=='Informasi Hasil Pengawasan')
        numbered=[p for p in ps[a+1:b] if p.tag==Q('p') and p.find('./'+Q('pPr')+'/'+Q('numPr')) is not None]
        if numbered:
            proto=deepcopy(numbered[0]);idx=body.index(numbered[0])
            for p in numbered:body.remove(p)
            for i,value in enumerate(lines(m['narratives']['METODOLOGI'])):
                p=deepcopy(proto)
                for node in p.xpath('.//w:t',namespaces=NS):node.text=''
                node=p.find('.//'+Q('t'));node.text=re.sub(r'^\d+[.)]\s*','',value);body.insert(idx+i,p)
        rows_replace(ts[0],[[i]+r for i,r in enumerate(m['tables']['PROSES_BISNIS'],1)])
        rows_replace(ts[1],[[i]+r for i,r in enumerate(m['tables']['RISIKO_KLIEN'],1)])
        rows_replace(ts[2],[[i]+r for i,r in enumerate(m['tables']['RISIKO_PENUGASAN'],1)])
    if num==11:
        table=ts[0];old=[r for r in table.findall(Q('tr')) if re.search(r'\{\{KODE_UJI_\d+\}\}',text(r))];idx=table.index(old[0]);proto=deepcopy(old[0])
        for r in old:table.remove(r)
        for i,row in enumerate(m['tables']['PROGRAM_KERJA']):
            code,desc,steps,who,jam,hp,ref=row;r=deepcopy(proto)
            for c,val in zip(r.findall(Q('tc')),['',fmt(code)+'\n'+fmt(desc),steps,who,fmt(jam),fmt(round(hp,2)),'','',ref]):set_cell(c,val)
            cant=r.find('./'+Q('trPr')+'/'+Q('cantSplit'))
            if cant is not None and len(fmt(steps))>1200:cant.getparent().remove(cant)
            table.insert(idx+i,r)
        for r in table.findall(Q('tr')):
            for token in ['JP','JS','JK','JL','JT']:
                if '{{'+token+'}}' in text(r):
                    cells=r.findall(Q('tc'));set_cell(cells[5],fmt(round(float(v[token].replace(',','.'))/m['jam_day'],2)))
                    phase=0 if token=='JP' else 1 if token=='JS' else 2
                    set_cell(cells[3],'\n'.join(p['name'] for p in team if p['hours'][phase]>0) if token!='JT' else '')
    if num==12:
        rows_replace(ts[0],full)
        for table,subset,start in [(ts[1],team[:6],1),(ts[2],team[6:],7)]:
            rows_replace(table,[[i,p['name'],p['role'],str(i)+'.' if i%2 else '',str(i)+'.' if not i%2 else ''] for i,p in enumerate(subset,start)])
        if len(team)<=6:ts[2].getparent().remove(ts[2]);collapse_section(root)

def fill_docx(source,destination,num,model,values):
    # Kunci = teks asli templat (TEMPLATE_IDENTITY), bukan profil_unit.json; bila profil diubah ke
    # unit lain, kop templat Papua Tengah tetap terganti.
    d=model['data']
    substitutions={TEMPLATE_IDENTITY[field]:fmt(d[key]) for key,field in PROFILE_FIELDS.items() if field!='kota'}
    substitutions[TEMPLATE_IDENTITY['kota']+',']=fmt(d['KOTA_UNIT'])+','
    with ZipFile(source) as zi,ZipFile(destination,'w',ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            payload=zi.read(item.filename)
            if item.filename.startswith('word/') and item.filename.endswith('.xml'):
                root=E.fromstring(payload)
                # Ganti identitas unit pada teks templat saja, sebelum isian pengguna masuk;
                # alamat objek seperti "Jl. Merdeka, Nabire," tidak boleh ikut berubah.
                for n in root.xpath('//w:t',namespaces=NS):
                    s=n.text or ''
                    for a,b in substitutions.items():s=s.replace(a,b)
                    n.text=s
                if item.filename=='word/document.xml':adapt_document(root,num,model,values)
                tokens(root,values)
                if TOKEN.search(text(root)):raise RuntimeError('Penanda isian tersisa pada '+item.filename)
                payload=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
            zo.writestr(item,payload)

def safe_title(name):
    value=re.sub(r'[<>:"/\\|?*\x00-\x1f]','-',name).strip().rstrip('.')
    if value.upper() in ['CON','PRN','AUX','NUL'] or re.fullmatch(r'(COM|LPT)[1-9]',value,re.I):value='Penugasan '+value
    if not value:raise InputError(['Nama penugasan tidak dapat dipakai sebagai judul folder.'])
    # Windows restricts a single path component to 255 UTF-16 code units.
    if len(value.encode('utf-16-le'))//2>230:value=value[:215].rstrip()+' - '+hashlib.sha256(name.encode()).hexdigest()[:8]
    return value

def generate(model,output_root,pdf=True):
    values=values_for(model);title=safe_title(fmt(model['data']['NAMA_PENUGASAN']))
    assignment=Path(output_root).resolve()/title;dest=assignment
    if dest.exists():dest=assignment/('Versi_'+datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
    if dest.exists():raise FileExistsError(dest)
    output_root=Path(output_root).resolve();output_root.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.mpp-build-',dir=output_root) as tmp:
        stage=Path(tmp);records=[]
        for source in sorted((ROOT/'assets'/'templates').glob('*.docx')):
            num=int(source.name[:2])
            if num==9 and model['jenis']=='PIA':continue
            external=model['files'].get(num)
            target=stage/(source.stem+external.suffix.lower() if external else source.name)
            if external:shutil.copy2(external,target)
            else:fill_docx(source,target,num,model,values)
            records.append({'number':num,'file':target.name,'source':str(external or source),'method':'salinan output/sumber' if external else 'isian templat','sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
        rendered=render_documents(stage) if pdf else []
        layout=[f"{r['file']}: {e}" for r in rendered for e in r['layout_errors']]
        if layout:raise InputError(layout)
        manifest={'schema_version':VERSION,'nama_penugasan':fmt(model['data']['NAMA_PENUGASAN']),'jenis_penugasan':model['jenis'],'jalur_st':model['jalur'],'output_folder':str(dest),'input_file':str(model['workbook']),'input_sha256':hashlib.sha256(model['workbook'].read_bytes()).hexdigest(),'count':len(records),'documents':records,'render':rendered,'pia_report_required':model['jenis']!='PIA','traceability':model['traceability'],'notes':['Paket perencanaan/konsep; tidak mengklaim telah disahkan.','Tanggal checklist merupakan rencana; kolom bukti pelaksanaan, paraf, dan realisasi tidak diisi otomatis.','Status TERSEDIA mengikuti pernyataan pengguna pada file isian.','Periksa visual hasil render sebelum menyerahkan paket untuk reviu.','Data eksternal SIMA-NG/laporan PIA disalin utuh; cocokkan substansi sumber tersebut dengan isian.']}
        (stage/'Rancangan_MPP.json').write_text(json.dumps(model['plan'],ensure_ascii=False,indent=2),encoding='utf-8')
        matrix=['# Pemetaan Insilwas, Risiko Klien, TAO/TEO, dan KM 6','','| Insilwas | Risiko klien | TAO/TEO | Task | Pelaksana |','|---|---|---|---|---|']
        for step in model['traceability']:
            matrix.append('| '+' | '.join(', '.join(step[k]).replace('|','/') for k in ['ihp_ids','risk_ids','objective_ids'])+' | '+step['id']+' | '+', '.join(step['assignees']).replace('|','/')+' |')
        (stage/'Pemetaan_Insilwas_Risiko_Tujuan_Tugas.md').write_text('\n'.join(matrix)+'\n',encoding='utf-8')
        (stage/'Manifest_MPP.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
        (stage/'Ringkasan_Paket.md').write_text('# '+fmt(model['data']['NAMA_PENUGASAN'])+'\n\n'+f"Jenis: {model['jenis']}. Jumlah dokumen: {len(records)}.\n\n"+('Laporan hasil PIA tidak menjadi prasyarat ST PIA dan tidak dibuat dalam paket ini.\n' if model['jenis']=='PIA' else 'Laporan hasil PIA dibuat manual/digunakan dari sumber sebelumnya sebagai dasar DPP.\n')+'\nSurat pengantar dibuat manual DOCX. Blok tanda tangan tetap kosong untuk pengesahan.\n\n'+ '\n'.join('- '+r['file'] for r in records)+'\n',encoding='utf-8')
        dest.mkdir(parents=True,exist_ok=False)
        try:
            for item in stage.iterdir():
                if item.is_dir():shutil.copytree(item,dest/item.name)
                else:shutil.copy2(item,dest/item.name)
        except Exception:
            # Retain incomplete files for diagnosis; never recursively remove a user target.
            (dest/'PEMBUATAN_BELUM_SELESAI.txt').write_text('Penyalinan hasil terhenti. Gunakan versi baru setelah masalah terselesaikan.',encoding='utf-8');raise
    return manifest

def main():
    p=argparse.ArgumentParser(description='Buat seluruh paket MPP dari workbook isian.');p.add_argument('workbook',type=Path)
    p.add_argument('--content',type=Path,help='Rancangan risiko/DPP/KM 6 yang disusun otomatis oleh skill, bukan isian pengguna');p.add_argument('--inspect',action='store_true',help='Baca fakta dan anggaran untuk penyusunan rancangan');p.add_argument('--output-root',type=Path,default=Path('Hasil_MPP'),help='Folder induk hasil (default: Hasil_MPP pada folder kerja)');p.add_argument('--check',action='store_true',help='Preflight saja, tanpa folder hasil')
    p.add_argument('--no-pdf',action='store_true');p.add_argument('--cached',action='store_true',help='Gunakan cache yang sudah dihitung Excel; tanpa mengubah file sumber')
    a=p.parse_args()
    try:
        model=read_model(a.workbook,recalc=not a.cached,content=a.content,inspect_only=a.inspect)
        if a.inspect:result={'status':'facts_ready','input_sha256':model['input_sha256'],'data':model['data'],'team':model['team'],'ihp':model['ihp'],'sources':model['sources'],'files':model['files'],'phase_hours':model['stages']}
        elif a.check:result={'status':'ready','jenis':model['jenis'],'personnel':len(model['team']),'documents':11 if model['jenis']=='PIA' else 12,'total_hours':sum(model['stages'])}
        else:result={'status':'created',**generate(model,a.output_root,pdf=not a.no_pdf)}
        print(json.dumps(result,ensure_ascii=False,default=str));return 0
    except InputError as e:print(json.dumps({'status':'incomplete','issues':e.issues},ensure_ascii=False));return 2
    except Exception as e:print(json.dumps({'status':'error','message':str(e)},ensure_ascii=False));return 1

if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
