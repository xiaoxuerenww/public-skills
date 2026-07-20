---
name: sanitize-pii
description: "Scan directories for personal information and PII, then replace or remove sensitive data. Use when preparing code/docs for public release, sanitizing examples, or removing identifying information from shared materials."
---

# Sanitize PII

**Purpose:** Scan a directory for personal information and PII, report findings, and systematically replace or remove sensitive data.

**Use when:** Preparing private materials for public release, sanitizing example code/docs, removing identifying information before sharing, or auditing a codebase for leaked credentials.

## PII Categories

This skill scans for:

1. **Names** — Personal names in code/docs/comments
2. **Email addresses** — Pattern: `*@*.com`, `*@*.org`, etc.
3. **Phone numbers** — Pattern: `\d{3}[-.]?\d{3}[-.]?\d{4}` and variations
4. **Absolute paths** — Home directories, username-specific paths
5. **Credentials** — API keys, tokens, passwords, secrets, SSH keys
6. **Domain-specific identifiers** — Company names, project names, internal URLs
7. **Sensitive metadata** — Compensation, interview feedback, personal notes

## Modes

### Scan Mode (default)

Report PII findings without making changes.

**Trigger:** User asks to scan, audit, check for PII, or find sensitive info.

**Steps:**

1. **Resolve target directory**
   - If user provides a path, use it
   - If user provides a file, use its parent directory
   - Otherwise use current working directory

2. **Define file scope**
   - Default: `*.md`, `*.py`, `*.js`, `*.ts`, `*.json`, `*.yaml`, `*.yml`, `*.txt`
   - Exclude: `.git/`, `node_modules/`, `.venv/`, `__pycache__/`, `*.pyc`, `.env` files (flag separately)
   - Ask user for custom patterns if needed

3. **Scan for PII using grep patterns**

   ```bash
   # Names (if user provides a list)
   grep -rniE '(name1|name2|name3)' <dir> --include=<patterns>
   
   # Email addresses
   grep -rniE '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' <dir> --include=<patterns>
   
   # Phone numbers
   grep -rniE '\b\d{3}[-.]?\d{3}[-.]?\d{4}\b' <dir> --include=<patterns>
   
   # Absolute paths with username
   grep -rniE '/Users/[^/]+|/home/[^/]+|C:\\Users\\[^\\]+' <dir> --include=<patterns>
   
   # Credentials keywords
   grep -rniE '(password|api.key|secret|token|credential|private.key|ssh.key)' <dir> --include=<patterns>
   
   # Company/domain-specific (if user provides)
   grep -rniE '(company1|company2|internal.url.com)' <dir> --include=<patterns>
   ```

4. **Generate scan report**

   Write to `pii_scan_report.md` in the target directory:

   ```markdown
   # PII Scan Report
   
   **Directory:** <dir>
   **Scan date:** <date>
   **Files scanned:** <count>
   
   ## Findings
   
   ### Names
   - `name1`: <count> occurrences in <files>
   - `name2`: <count> occurrences in <files>
   
   ### Email Addresses
   - `email@example.com`: <count> occurrences in <files>
   
   ### Phone Numbers
   - `555-123-4567`: found in <files>
   
   ### Absolute Paths
   - `/Users/username/...`: <count> occurrences in <files>
   
   ### Credentials
   - `password`: <count> occurrences in <files>
   - `api_key`: <count> occurrences in <files>
   
   ### Company-Specific
   - `CompanyName`: <count> occurrences in <files>
   
   ## Recommendations
   
   - Replace names with: "the user", "user", or generic role names
   - Replace emails with: placeholders or remove
   - Replace phone numbers with: `XXX-XXX-XXXX` or remove
   - Replace absolute paths with: `$HOME`, `/Users/$USER`, or relative paths
   - Replace credentials with: `<REDACTED>`, `YOUR_API_KEY_HERE`, or environment variable references
   - Replace company names with: generic terms or `<COMPANY>`
   
   ## Next Steps
   
   Run in sanitize mode to apply replacements.
   ```

5. **Present summary to user**
   - Count of PII types found
   - High-severity items (credentials, emails, phone numbers)
   - Path to full report
   - Suggest sanitize mode if PII found

### Sanitize Mode

Apply systematic PII replacements.

**Trigger:** User asks to sanitize, clean, redact, or remove PII.

**Steps:**

1. **Run scan mode first** (if not already done)

2. **Build replacement map**

   Ask user for replacement strategy for each PII category:

   - **Names:**
     - Option 1: Replace with "the user" (default)
     - Option 2: Replace with role ("developer", "admin")
     - Option 3: Replace with placeholder ("USER_NAME")
     - Option 4: Keep as-is

   - **Email addresses:**
     - Option 1: Replace with `user@example.com` (default)
     - Option 2: Replace with `<EMAIL>`
     - Option 3: Remove entirely
     - Option 4: Keep as-is

   - **Phone numbers:**
     - Option 1: Replace with `XXX-XXX-XXXX` (default)
     - Option 2: Remove entirely
     - Option 3: Keep as-is

   - **Absolute paths:**
     - Option 1: Replace `/Users/username` with `/Users/$USER` (default)
     - Option 2: Replace with relative paths
     - Option 3: Replace with `$HOME`
     - Option 4: Keep as-is

   - **Credentials:**
     - Option 1: Replace with `<REDACTED>` (default)
     - Option 2: Replace with placeholder like `YOUR_API_KEY_HERE`
     - Option 3: Replace with environment variable reference
     - Option 4: Flag for manual review (do not auto-replace)

   - **Company-specific:**
     - Option 1: Replace with generic terms (default)
     - Option 2: Replace with `<COMPANY>`
     - Option 3: Keep as-is

3. **Create backup**

   ```bash
   tar -czf <dir>_backup_<timestamp>.tar.gz <dir>
   ```

4. **Apply replacements**

   Use `sed` to replace in-place:

   ```bash
   # Example: Replace name
   find <dir> -type f \( -name "*.md" -o -name "*.py" ... \) \
     -exec sed -i '' -e "s/Julie's/the user's/g" -e "s/Julie/the user/g" {} +
   
   # Example: Replace paths
   find <dir> -type f \( -name "*.md" -o -name "*.py" ... \) \
     -exec sed -i '' -e 's|/Users/username|/Users/\$USER|g' {} +
   
   # Example: Replace emails
   find <dir> -type f \( -name "*.md" -o -name "*.py" ... \) \
     -exec sed -i '' -e 's|real@email.com|user@example.com|g' {} +
   ```

5. **Verify replacements**

   Re-run grep searches to confirm:
   - Original PII patterns no longer found
   - Replacement patterns appear as expected

6. **Generate sanitization report**

   Write to `pii_sanitization_report.md`:

   ```markdown
   # PII Sanitization Report
   
   **Directory:** <dir>
   **Date:** <date>
   **Backup:** <backup_file>
   
   ## Replacements Applied
   
   ### Names
   - "Julie" → "the user" (<count> files changed)
   
   ### Email Addresses  
   - "real@email.com" → "user@example.com" (<count> files)
   
   ### Paths
   - "/Users/username" → "/Users/$USER" (<count> files)
   
   ### Credentials
   - "api_key: sk-xxx" → "api_key: <REDACTED>" (<count> files)
   
   ## Verification
   
   - [x] Original PII patterns: 0 remaining
   - [x] Backup created: <path>
   - [x] Replacements verified
   
   ## Files Modified
   
   - file1.md
   - file2.py
   - ...
   ```

7. **Present summary**
   - Count of files modified
   - Path to backup
   - Path to sanitization report
   - Verification status

### Interactive Mode

Step-by-step guided sanitization with user approval for each category.

**Trigger:** User asks for interactive, guided, or step-by-step sanitization.

**Steps:**

1. Run scan mode
2. For each PII category found:
   - Show example occurrences (first 5)
   - Ask user for replacement strategy
   - Preview one file's changes
   - Get confirmation before applying
3. Apply approved replacements
4. Generate report

## File Patterns

**Include by default:**
- `*.md`, `*.py`, `*.js`, `*.ts`, `*.tsx`, `*.jsx`
- `*.json`, `*.yaml`, `*.yml`
- `*.txt`, `*.sh`, `*.bash`
- `*.java`, `*.go`, `*.rb`, `*.php`

**Exclude by default:**
- `.git/`, `.svn/`, `.hg/`
- `node_modules/`, `bower_components/`
- `.venv/`, `venv/`, `env/`, `virtualenv/`
- `__pycache__/`, `*.pyc`, `*.pyo`
- `.DS_Store`, `Thumbs.db`
- Binary files, images, compiled code

**Flag for manual review (never auto-replace):**
- `.env`, `.env.*` files
- `credentials.*`, `secrets.*`
- `*.key`, `*.pem`, `*.crt`

## Safety Rules

1. **Always create backup** before sanitizing
2. **Never auto-replace** in `.env` or credential files — flag only
3. **Confirm destructive operations** with user
4. **Preserve context** — replacements should make sense in context
5. **Verify post-sanitization** — re-scan to confirm PII removed
6. **Report what changed** — detailed log of all modifications

## Common Patterns

### Names
- Possessive: `Name's` → `the user's`
- Subject: `Name did X` → `the user did X`
- Object: `help Name` → `help the user`

### Paths
- macOS: `/Users/username` → `/Users/$USER`
- Linux: `/home/username` → `/home/$USER` or `$HOME`
- Windows: `C:\Users\username` → `C:\Users\$env:USERNAME`

### Credentials
- API keys: `api_key: sk-...` → `api_key: <REDACTED>`
- Tokens: `token: ghp_...` → `token: YOUR_TOKEN_HERE`
- Passwords: `password: xyz` → `password: <REDACTED>`

### Emails
- Real: `real@email.com` → `user@example.com`
- Inline: `email: real@email.com` → `email: <EMAIL>`

### Phone Numbers
- US format: `555-123-4567` → `XXX-XXX-XXXX`
- International: `+1-555-123-4567` → `+X-XXX-XXX-XXXX`

## Example Usage

**Scan a directory:**
```
User: "Scan ml-interview for PII"
Assistant: [runs scan mode, generates report, presents summary]
```

**Sanitize with defaults:**
```
User: "Sanitize ml-interview directory"
Assistant: [scans, asks for confirmation on defaults, creates backup, applies replacements, verifies]
```

**Interactive sanitization:**
```
User: "Interactively sanitize my-project/"
Assistant: [scans, shows each PII type, asks for replacement choice, previews changes, applies with approval]
```

## Output Artifacts

- `pii_scan_report.md` — Detailed scan findings
- `pii_sanitization_report.md` — What was changed
- `<dir>_backup_<timestamp>.tar.gz` — Pre-sanitization backup
- Modified files in place

## Notes

- **Idempotent:** Re-running sanitize with same config should make no additional changes
- **Reversible:** Backup allows full restoration
- **Auditable:** Reports provide complete change log
- **Conservative:** When in doubt, flag for manual review rather than auto-replace
- **Context-aware:** Replacement suggestions consider file type and context
