# Drive Audit Repository - AI Coding Assistant Instructions

## Architecture Overview

This is a **specialized drive audit repository** that tracks selective parts of a Windows C:\ drive using Git. The entire C:\ drive serves as the working directory, but only allowlisted folders are tracked through an inverse `.gitignore` pattern.

**Key Concept**: Instead of tracking a typical project structure, this repo monitors specific user folders and config directories on a Windows system while defensively excluding system files, large directories, and sensitive areas.

## Critical Workflows

### Safe Git Operations
```bash
# ALWAYS check what would be added before staging
git status --porcelain
git diff --name-only --cached

# Use selective staging for large changesets
git add -p    # Interactive staging
git add --dry-run .   # Preview what would be added

# Defensive status checking
git clean -n -d      # Show what would be cleaned (never run without -n)
```

### Repository Maintenance
```bash
# Check repository size and object count
git count-objects -vH
du -sh .git/

# Audit what's actually being tracked
git ls-files | head -20
git ls-files --cached --others --exclude-standard
```

## Windows-Specific Considerations

### PowerShell Integration
- Use `git status` in PowerShell with UTF-8 encoding: `$OutputEncoding = [Text.UTF8Encoding]::UTF8`
- Watch for Windows path separator issues in scripts
- Be aware of Windows file locking when Git operations touch active files

### File System Patterns
- `.gitignore` uses both forward and backslash patterns for Windows compatibility
- System files (pagefile.sys, hiberfil.sys) are explicitly blocked
- AppData directories are defensively excluded to prevent credential exposure

## Project-Specific Patterns

### Defensive Exclusion Strategy
```gitignore
# Block everything by default
/*

# Explicitly allow curated folders
!/Projects/
!/Docs/
!/Scripts/

# Defense-in-depth blocking
Windows/
Program Files/
**/.git/
**/node_modules/
```

### Allowlisted Directories
- `Projects/` - Development work
- `Docs/` - Documentation and notes  
- `Scripts/` - Automation and utility scripts
- `Config/` - Configuration files
- `Users/Ajpad/Documents/` - User documents
- `Users/Ajpad/Desktop/` - Desktop files

## Common Pitfalls

1. **Never run `git add .` blindly** - could stage system files or large directories
2. **Always verify `.gitignore` changes** - incorrect patterns could expose sensitive data
3. **Monitor repo size growth** - unintended tracking of large files is expensive
4. **Check for credential exposure** - Windows stores credentials in predictable locations

## Integration Points

- **Windows File System**: Direct integration with NTFS permissions and file attributes
- **User Environment**: Tracks personal workspace and configuration changes
- **System State**: Monitors configuration drift and manual changes outside version control

## Key Files to Understand

- `.gitignore` - The inverse allowlist pattern that defines what gets tracked
- `CDriveRules.md` - Documentation of allowlist rules and rationale (if present)
- Any PowerShell scripts in tracked directories that automate Git operations

## Working with This Repository

When making changes:
1. Understand you're working in C:\ root, not a typical project directory
2. Use relative paths carefully - they resolve from C:\ 
3. Test `.gitignore` changes with `git check-ignore -v <path>` 
4. Regularly audit tracked files to prevent unintended exposure

This unique architecture requires careful, defensive Git practices to maintain security and performance while providing visibility into selective file system changes.