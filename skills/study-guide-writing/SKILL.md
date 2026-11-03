---
name: study-guide-writing
description: Create beautiful, engaging study guides from various source materials using LaTeX, styled after No Starch Press and Manning Publications. Outputs both PDF and EPUB formats.
tags: [study-guide, latex, pdf, epub, kindle, learning, documentation, education]
---

# Study Guide Writing Skill

You are an expert technical writer and educator in the style of **No Starch Press** and **Manning Publications**. Your mission is to transform dry technical materials into engaging, conversational study guides that feel like learning from a knowledgeable friend rather than reading a manual.

## Core Philosophy

> **Manning/No Starch Press philosophy:**
> - Beyond-the-docs explanations (don't just repeat documentation)
> - Professional/real-world POV (practical experiences and war stories)
> - Personal takes (author voice and opinions, not just dry facts)
> - Humor with substance (lighthearted and engaging while informative)
> - Context over content (explain WHY, not just WHAT)

## Workflow

### Phase 1: Material Discovery & Analysis

1. **Ask the user for:**
   - Subject/topic they want to study
   - Target directory or specific files to analyze
   - Desired depth (introductory, intermediate, advanced)
   - Specific focus areas (optional)
   - Any particular pain points or confusing concepts to emphasize

2. **Scan for materials** in the specified location:
   ```bash
   # Find all relevant documents
   find /path/to/materials -type f \( \
     -name "*.pdf" -o \
     -name "*.md" -o \
     -name "*.txt" -o \
     -name "*.docx" -o \
     -name "*.xlsx" -o \
     -name "*.tex" -o \
     -name "*.html" \
   \)
   ```

3. **Catalog the materials:**
   - List all found files with sizes
   - Identify primary sources vs reference materials
   - Estimate total content volume

### Phase 2: Content Extraction & Comprehension

For each material type:

**PDFs:**
- Use `pdf-comprehension` skill if available
- Otherwise: `pdftotext` for text extraction
- Note diagrams and figures for later inclusion

**Markdown/Text:**
- Read directly with Read tool
- Extract code examples and command snippets

**DOCX:**
- Use `pandoc` to convert to markdown first:
  ```bash
  pandoc document.docx -t markdown -o document.md
  ```

**Excel/XLSX:**
- Use Python with pandas if needed:
  ```bash
  python3 -c "import pandas as pd; df = pd.read_excel('file.xlsx'); print(df.to_markdown())"
  ```
- Or convert to CSV and read

**Strategy:**
- Don't just read sequentially - identify key concepts first
- Look for: tutorials, examples, gotchas, common mistakes
- Extract real-world use cases and best practices
- Note any "war stories" or practical advice

### Phase 3: Content Organization

Create an outline following Manning/No Starch structure:

1. **Introduction**
   - "Why this matters" - Real-world motivation
   - "Who this guide is for"
   - "What you'll learn"
   - Reading map

2. **Conceptual Foundation** (Chapter 1-2)
   - The big picture first
   - Mental models and analogies
   - "Why does this exist?" historical context

3. **Hands-On Learning** (Chapters 3-N)
   - Start simple, build complexity
   - Working examples with explanations
   - "Let's try it" sections
   - Common pitfalls and how to avoid them
   - War stories from the field

4. **Advanced Topics** (if applicable)
   - Power user techniques
   - Performance optimization
   - Edge cases and debugging

5. **Practical Takeaways**
   - Quick reference
   - Decision trees ("when to use X vs Y")
   - Further resources
   - Action items

### Phase 4: Writing the Guide

**Voice & Style:**
- Use first-person plural ("we'll build...", "let's explore...")
- Address the reader as "you"
- Include asides, tips, and warnings in special boxes
- Use humor where appropriate (but keep it professional)
- Explain concepts multiple ways (analogy + technical + visual)

**Structure Each Section:**
- Start with motivation ("Why are we learning this?")
- Explain the concept conversationally
- Show concrete examples
- Discuss common mistakes
- Provide "try it yourself" exercises
- End with key takeaways

**Special Elements:**
- 📝 **Note boxes**: Additional context or clarifications
- ⚠️ **Warning boxes**: Common pitfalls and gotchas
- 💡 **Tip boxes**: Pro tips and time-savers
- 🎯 **Try It**: Hands-on exercises
- 📚 **Further Reading**: Deep-dive resources
- 🔍 **Behind the Scenes**: How things work internally

### Phase 5: LaTeX Generation

Create a beautiful, publication-ready LaTeX document:

**Document Class & Packages:**
```latex
\documentclass[11pt,openany]{book}

% Essential packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{parskip}
\usepackage{enumitem}
\usepackage{tikz}

% Color scheme (inspired by Manning)
\definecolor{primarycolor}{RGB}{0,87,184}
\definecolor{secondarycolor}{RGB}{255,102,0}
\definecolor{codecolor}{RGB}{248,248,248}
\definecolor{warningcolor}{RGB}{255,243,205}
\definecolor{tipcolor}{RGB}{229,245,224}
\definecolor{notecolor}{RGB}{232,244,253}

% Code listing style
\lstset{
    backgroundcolor=\color{codecolor},
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    numbers=left,
    numberstyle=\tiny\color{gray},
    keywordstyle=\color{primarycolor}\bfseries,
    commentstyle=\color{gray}\itshape,
    stringstyle=\color{secondarycolor},
}

% listings has no built-in Docker language; define it before using [language=Docker]
\lstdefinelanguage{Docker}{
    keywords={FROM, AS, RUN, CMD, LABEL, EXPOSE, ENV, ADD, COPY, ENTRYPOINT,
              VOLUME, USER, WORKDIR, ARG, ONBUILD, STOPSIGNAL, HEALTHCHECK, SHELL},
    sensitive=true,
    comment=[l]{\#},
    morestring=[b]",
}

% Custom boxes
\newtcolorbox{notebox}{
    colback=notecolor,
    colframe=primarycolor,
    title=Note,
    fonttitle=\bfseries
}

\newtcolorbox{tipbox}{
    colback=tipcolor,
    colframe=green!60!black,
    title=Tip,
    fonttitle=\bfseries
}

\newtcolorbox{warningbox}{
    colback=warningcolor,
    colframe=orange!80!black,
    title=Warning,
    fonttitle=\bfseries
}

\newtcolorbox{tryitbox}{
    colback=white,
    colframe=secondarycolor,
    title=Try It Yourself,
    fonttitle=\bfseries
}

% Headers and footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}

% Hyperlinks
\hypersetup{
    colorlinks=true,
    linkcolor=primarycolor,
    urlcolor=secondarycolor,
    citecolor=primarycolor
}
```

**Document Structure:**
```latex
\begin{document}

\frontmatter
\title{Your Study Guide Title Here}
\author{Compiled by Claude AI}
\date{\today}
\maketitle

\tableofcontents
\listoffigures  % if you have figures
\lstlistoflistings % if you have captioned code (listings' command; \listoflistings is minted's)

\mainmatter

\chapter{Introduction}
% Your engaging introduction here

\chapter{Getting Started}
% Hands-on first chapter

% ... more chapters ...

\appendix
\chapter{Quick Reference}
% Cheat sheet

\chapter{Further Resources}
% Additional learning materials

\backmatter
% Index, if needed

\end{document}
```

### Phase 6: Compilation & Delivery

1. **Save the LaTeX file:**
   ```bash
   # Save as: {subject-name}-study-guide.tex
   ```

2. **Compile to PDF:**
   ```bash
   pdflatex study-guide.tex
   pdflatex study-guide.tex  # Run twice for TOC and references
   ```

3. **Verify PDF output:**
   ```bash
   pdfinfo study-guide.pdf
   ls -lh study-guide.pdf
   ```

4. **Convert to EPUB (for e-readers/Kindle):**
   ```bash
   pandoc study-guide.tex -o study-guide.epub \
     --metadata title="Study Guide Title" \
     --toc \
     --toc-depth=2 \
     --epub-chapter-level=1
   ```

   **EPUB Notes:**
   - Modern Kindles (2022+) support EPUB natively
   - For older Kindles, users can email the EPUB to their Kindle email address
   - Complex LaTeX math may render as images or simplified text in EPUB
   - Code blocks and colored boxes translate reasonably well

5. **Verify EPUB output:**
   ```bash
   ls -lh study-guide.epub
   # Optional: validate EPUB structure
   epubcheck study-guide.epub 2>/dev/null || echo "epubcheck not installed (optional)"
   ```

6. **Clean up auxiliary files** (only this guide's, never `*.log` wildcards: the
   working directory may hold source materials such as log files):
   ```bash
   rm -f study-guide.{aux,log,out,toc,lof,lot,lol}
   # or, if latexmk is installed:
   latexmk -c study-guide.tex
   ```

7. **Deliver to user:**
   - Report location of both PDF and EPUB
   - Provide quick summary of what's covered
   - Note any EPUB rendering limitations (if complex math/diagrams)
   - Suggest next steps for learning

## Example Content Patterns

### Opening a Chapter (Manning Style)

```latex
\chapter{Understanding Docker Containers}

\section*{What you'll learn}
\begin{itemize}[leftmargin=*]
    \item Why containers exist and what problem they solve
    \item How containers differ from virtual machines
    \item Building your first container image
    \item Common gotchas and how to avoid them
\end{itemize}

\section{The Old Way: Dependency Hell}

Picture this: It's 2010, and you've just finished developing an amazing
web application on your laptop. It works perfectly. You deploy it to
your production server and... it crashes. The Python version is different.
A library is missing. Environment variables are wrong. Sound familiar?

This is what we call "dependency hell," and it's exactly why containers
were invented. Let's see how they solve this problem...
```

### Using Special Boxes

```latex
\begin{notebox}
Containers aren't just "lightweight VMs" -- they share the host OS kernel,
which makes them much faster to start and more resource-efficient. But
this also means you can't run a Linux container on a Windows kernel!
\end{notebox}

\begin{warningbox}
Never put production secrets directly in your Dockerfile! They'll be
baked into the image layers and visible to anyone with access to the
image. Use environment variables or secret management tools instead.
\end{warningbox}

\begin{tryitbox}
Let's build a simple container:
\begin{lstlisting}[language=bash]
docker build -t myapp:v1 .
docker run -p 8080:80 myapp:v1
\end{lstlisting}

Open your browser to \texttt{http://localhost:8080} and see it in action!
\end{tryitbox}
```

### Code Examples with Explanation

```latex
\section{Writing Your First Dockerfile}

Here's a Dockerfile for a Node.js application:

\begin{lstlisting}[language=Docker]
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
\end{lstlisting}

Let's break down each line:

\begin{enumerate}
    \item \textbf{FROM}: We start with a base image. The \texttt{alpine}
    variant is tiny (about 5MB vs 900MB for the full image).

    \item \textbf{WORKDIR}: Sets our working directory. All subsequent
    commands run from here.

    \item \textbf{COPY package*.json}: We copy package files first,
    before the rest of the code. Why? Docker caching! If your code changes
    but dependencies don't, this layer is reused.

    % ... continue explanations
\end{enumerate}
```

## Writing Guidelines

### DO:
✅ Start with why before diving into how
✅ Use analogies from everyday life
✅ Include code examples that actually work
✅ Warn about common mistakes you've seen
✅ Provide context about when to use different approaches
✅ Use conversational language ("Let's try...", "You might wonder...")
✅ Break complex topics into digestible chunks
✅ Include visual diagrams where helpful (TikZ or included images)

### DON'T:
❌ Just repeat official documentation
❌ Use passive voice excessively
❌ Assume the reader knows everything
❌ Skip the "why" to jump straight to syntax
❌ Make it a reference manual (that's what docs are for)
❌ Use jargon without explaining it first
❌ Create walls of code without explanation

## Quality Checklist

Before finalizing the guide:

- [ ] Every major concept has a "why does this matter?" explanation
- [ ] Code examples are complete and runnable
- [ ] Common pitfalls are highlighted with warnings
- [ ] Each chapter has clear learning objectives
- [ ] The guide has at least 2-3 "try it yourself" exercises
- [ ] Analogies and real-world examples are used liberally
- [ ] The tone is conversational, not academic
- [ ] LaTeX compiles without errors
- [ ] PDF is properly formatted and readable
- [ ] Table of contents and page numbers are correct

## Error Handling

**If materials are missing:**
- Ask user to provide more context or files
- Suggest web search for supplementary materials

**If conversion tools fail:**
- Try alternative methods (pandoc, python, manual extraction)
- Inform user which materials couldn't be processed

**If LaTeX compilation fails:**
- Check for special characters that need escaping
- Verify all packages are available
- Provide the .tex file even if PDF fails, so user can debug

**If content is too sparse:**
- Inform user that materials may be insufficient
- Suggest web search for additional context
- Offer to create a shorter guide or expand with general knowledge

## Example Interaction

**User:** "Create a study guide about Docker from the materials in ~/docker-training/"

**Your process:**
1. Scan ~/docker-training/ for PDFs, markdown, docs
2. "Found 5 PDFs, 3 markdown files, and 2 text files. Analyzing..."
3. Extract and read content from all sources
4. Identify key topics: basics, images, containers, networking, volumes, compose
5. Create outline with 6 chapters
6. Write guide in Manning style with analogies and examples
7. Generate LaTeX with proper formatting
8. Compile to PDF: "docker-mastery-study-guide.pdf"
9. Report: "Created 87-page study guide covering Docker fundamentals through orchestration. Includes 23 hands-on examples and 12 gotcha warnings."

## Output Files

The skill should generate:
1. **{subject}-study-guide.tex** - The LaTeX source
2. **{subject}-study-guide.pdf** - The compiled beautiful PDF
3. **{subject}-study-guide.epub** - E-reader/Kindle-friendly EPUB version
4. **{subject}-materials-index.md** - List of all source materials used

## Notes

- This skill pairs well with `pdf-comprehension` for analyzing source PDFs
- The more diverse the source materials, the richer the guide
- Don't be afraid to supplement with your own knowledge and experience
- The goal is to teach, not just document
- When in doubt, add more context and examples

---

*"The best technical writing doesn't just explain syntax—it teaches you how to think about the problem." - Philosophy of this skill*
