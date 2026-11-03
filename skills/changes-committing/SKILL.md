---
name: changes-committing
description: Securely commit code changes with credential checks, proper file filtering, and conventional commit messages. Use when user asks to commit changes, create a commit, or mentions committing code.
tags: [git, commit, security, credentials, conventional-commits]
---

# Changes Committing Skill

You are an expert at creating secure, well-formatted git commits that follow best practices and protect sensitive information.

## 🚨 CRITICAL SECURITY RULES 🚨

**NEVER commit files containing:**
- Hardcoded passwords, API keys, or secrets
- Real credentials in any form
- Kubernetes secrets with actual values
- Docker Compose files with hardcoded environment variables
- .env files with real values (only .env.example is safe)
- Test files with real authentication credentials

**ALWAYS check files before committing for these patterns!**

## When to Use This Skill

Use this skill when:
- User asks to "commit these changes"
- User says "create a commit" or "commit my work"
- User mentions "git commit" or committing code
- User wants to save their work to git

## Workflow

### Step 1: Analyze Current Changes

Run these commands in parallel:

```bash
# See all changed files
git status

# See staged changes
git diff --staged

# See unstaged changes (for context)
git diff

# Review recent commit style
git log --oneline -10
```

### Step 2: Security Screening (MANDATORY)

**Before doing anything else, scan for credentials.** Nothing may be staged yet at this
point, so scanning only `git diff --staged` would report "no credentials" for everything
you are about to add. Scan all tracked changes and the untracked files too:

```bash
# Tracked changes, staged and unstaged
git diff HEAD | grep -iE "(password|passwd|pwd|secret|api[_-]?key|token|credentials)" | grep -v "os\.Getenv\|process\.env\|ENV\[" || echo "No obvious credentials in tracked changes"

# Untracked files that would be added (respects .gitignore)
git ls-files --others --exclude-standard | while IFS= read -r f; do
  grep -inHE "(password|passwd|pwd|secret|api[_-]?key|token|credentials)" "$f"
done

# Check for suspicious patterns
git diff HEAD | grep -E '(".*[A-Za-z0-9]{32,}"|password.*=.*"[^$]|secret.*:.*")'
```

Run the staged-only scan again right before committing (Step 7) to confirm what is actually going in:

```bash
git diff --staged | grep -iE "(password|passwd|pwd|secret|api[_-]?key|token|credentials)" | grep -v "os\.Getenv\|process\.env\|ENV\[" || echo "No obvious credentials staged"
```

**Review each file being committed:**

For each file in git status:
1. If filename contains: `.env`, `secret`, `credential`, `auth`, `token`
   - 🚨 **STOP and review carefully**
   - If it contains real values: **DO NOT COMMIT**
   - Suggest moving to environment variables

2. If file is Kubernetes secret YAML/JSON:
   - Check for base64 encoded secrets
   - If real secrets: **DO NOT COMMIT**
   - Suggest: "Use Kubernetes secret management or sealed-secrets"

3. If file is docker-compose.yml or docker-compose.yaml:
   - Check environment sections for hardcoded values
   - If found: **DO NOT COMMIT**
   - Suggest: "Move to .env file and add .env to .gitignore"

4. If suspicious strings found:
   - Warn user: "Found potential credentials in [filename]"
   - Ask: "Are these dummy/example values or real credentials?"
   - If real: **REFUSE TO COMMIT** and suggest alternatives

### Step 3: File Filtering

**Automatically exclude from staging:**

1. **Internal documentation** (except README):
   ```bash
   # Do NOT stage these files:
   docs/*.md (except docs/README.md)
   NOTES.md
   TODO.md
   INTERNAL.md
   DISCUSSION.md
   MEETING_NOTES.md
   ```

2. **Credential files**:
   ```bash
   # Do NOT stage:
   .env (only .env.example is okay)
   secrets.yaml
   secrets.json
   *_credentials.json
   auth_config.json
   ```

3. **Test files with credentials**:
   ```bash
   # Do NOT stage:
   *_auth_test.go
   *_credentials_test.js
   test_auth_*.py
   ```

**If any of these are staged, unstage them:**

```bash
git reset HEAD <filename>
```

**Inform user which files were excluded and why.**

### Step 4: Suggest Credential Refactoring

If credentials are found in code, provide refactoring guidance:

**For hardcoded strings:**
```
❌ BAD:
  password: "mySecretPassword123"
  apiKey: "sk_live_1234567890abcdef"

✅ GOOD:
  password: process.env.DB_PASSWORD
  apiKey: os.getenv('API_KEY')

Action needed:
1. Move credentials to .env file
2. Add .env to .gitignore
3. Create .env.example with dummy values
4. Update code to read from environment
```

**For Docker Compose:**
```
❌ BAD:
  environment:
    - DB_PASSWORD=realPassword123
    - API_KEY=sk_live_abc123

✅ GOOD:
  environment:
    - DB_PASSWORD=${DB_PASSWORD}
    - API_KEY=${API_KEY}
  env_file:
    - .env

Action needed:
1. Create .env file with real values
2. Update docker-compose.yml to use ${VAR} syntax
3. Add .env to .gitignore
4. Create .env.example with dummy values
```

**For Kubernetes:**
```
❌ BAD:
  data:
    password: cGFzc3dvcmQxMjM=  # base64 of real password

✅ GOOD:
  Use external secret management:
  - Kubernetes Secrets (not in git)
  - Sealed Secrets
  - External Secrets Operator
  - HashiCorp Vault
  - Cloud provider secret managers
```

### Step 5: Determine Commit Type

Based on the changes, identify the conventional commit type:

- **feat**: New feature or functionality
- **fix**: Bug fix
- **docs**: Documentation only changes
- **style**: Code style/formatting (no logic change)
- **refactor**: Code restructuring without changing behavior
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Build system or dependencies
- **ci**: CI/CD configuration changes
- **chore**: Maintenance tasks, tooling

### Step 6: Write Commit Message

**Format**: `type(scope): concise description`

**Rules**:
1. **Keep first line under 72 characters**
2. **Use imperative mood**: "add feature" not "added feature"
3. **Be specific but concise**: Focus on what changed
4. **Emphasize notable changes**: What's most important?
5. **No co-author lines**: Never add "Co-Authored-By: Claude"
6. **No AI attribution**: Never add "Generated with Claude Code"
7. **Optional body**: Add details only if needed (after blank line)

**Good Examples**:
```
feat(auth): add JWT token refresh mechanism
fix(api): prevent null pointer in user lookup
refactor(db): extract connection logic to service
docs: update API endpoint documentation
chore(deps): upgrade express to v5.0.0
```

**Bad Examples** (don't do these):
```
❌ updated stuff
❌ fix bug
❌ changes
❌ feat: add authentication system with JWT tokens and refresh logic and session management
❌ feat(auth): add JWT tokens

Co-Authored-By: Claude <noreply@anthropic.com>  # NEVER ADD THIS
```

### Step 7: Stage and Commit

**Only stage safe files:**

```bash
# Stage specific safe files by name
git add <file1> <file2> <file3>
```

Do not use `git add .` / `git add -A` followed by unstaging: a `.env` or key file that is not in
`.gitignore` gets staged, and one forgotten `git reset` puts it in history.

**Create the commit:**

```bash
git commit -m "type(scope): description"
```

**For commits needing a body:**

```bash
git commit -m "type(scope): short description" -m "
Detailed explanation if needed:
- What changed and why
- Any breaking changes
- Related issue numbers
"
```

**Verify the commit:**

```bash
git log -1 --stat
```

### Step 8: Final Security Check

After committing, verify no secrets were committed:

```bash
# Check the commit content
git show HEAD | grep -iE "(password|secret|api[_-]?key|token)" | grep -v "ENV\|getenv\|process\.env"
```

If secrets found: **IMMEDIATELY tell user to:**
```bash
# Undo the commit (only safe while it has NOT been pushed)
git reset HEAD~1

# Fix the issue, then re-commit
```

If the commit was already pushed, undoing it locally is not enough: treat the secret as
leaked, tell the user to revoke/rotate it first, and only then clean the history.

## File Exclusion Patterns

**Always exclude these from commits:**

```
# Internal documentation
docs/*.md (except docs/README.md)
*.internal.md
NOTES.md
TODO.md
DISCUSSION.md
MEETING_NOTES.md
BRAINSTORM.md
WIP.md

# Credential files
.env
.env.local
.env.production
secrets.yaml
secrets.json
*_secrets.*
*_credentials.*
auth_config.*
service-account-key.json

# Test files with real credentials
*_auth_test.*
*_credentials_test.*
test_*_auth.*
```

**Exception: These are okay:**
```
README.md
docs/README.md
.env.example
.env.*.example
secrets.example.yaml
```

## Error Handling

**If staging fails:**
- Check git status for conflicts
- Resolve merge conflicts first
- Verify files exist and paths are correct

**If commit fails:**
- Check for pre-commit hooks
- Read hook error messages
- Address issues and retry

**If credentials detected:**
- STOP immediately
- Do NOT proceed with commit
- Guide user through refactoring
- Only commit after credentials removed

## Interaction Pattern

**Present findings to user:**

```
🔍 Analyzing changes...

Files changed:
✅ src/auth/login.js
✅ src/utils/validator.js
❌ docs/internal-discussion.md (excluded: internal doc)
❌ .env (excluded: contains credentials)
⚠️  docker-compose.yml (WARNING: check for hardcoded values)

Security scan: ✅ No obvious credentials in safe files
⚠️  Found hardcoded DB password in docker-compose.yml

RECOMMENDATION:
Move DB_PASSWORD to .env file:
1. Create .env with: DB_PASSWORD=your_password
2. Update docker-compose.yml to: DB_PASSWORD=${DB_PASSWORD}
3. Add .env to .gitignore

Proposed commit:
feat(auth): add JWT token validation

Staging:
- src/auth/login.js
- src/utils/validator.js

Proceed with commit? [After you fix docker-compose.yml]
```

## Best Practices

1. **Security first**: Always scan before committing
2. **Be selective**: Don't auto-stage everything
3. **Clear messages**: Make commits self-documenting
4. **Keep it simple**: One logical change per commit
5. **Verify after**: Check what was actually committed
6. **No attribution**: Keep commits professional and personal
7. **Protect credentials**: When in doubt, don't commit

## Commit Message Templates

**For features:**
```
feat(scope): add <what>

- Key point 1
- Key point 2
```

**For fixes:**
```
fix(scope): resolve <issue>

- What was wrong
- How it's fixed
```

**For refactoring:**
```
refactor(scope): improve <what>

- Why this change
- What improved
```

**For chores:**
```
chore(scope): update <what>

- Brief explanation
```

## Checklist

Before every commit, verify:

- [ ] No hardcoded credentials in staged files
- [ ] Internal docs excluded (except README)
- [ ] .env files not staged (only .env.example is okay)
- [ ] Docker/K8s secrets use environment variables
- [ ] Commit message follows conventional format
- [ ] Message is concise and descriptive
- [ ] No co-author or AI attribution lines
- [ ] Only relevant files staged
- [ ] Commit represents one logical change

## Notes

- This skill prioritizes security over convenience
- When unsure about a file, ask the user before committing
- Better to exclude too much than commit credentials
- Commit messages should be professional and team-ready
- No mention of AI assistance in git history

---

**Remember**: A secure commit is more important than a fast commit. Always check for credentials!
