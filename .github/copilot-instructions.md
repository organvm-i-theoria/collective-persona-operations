# Drive Audit Repository - AI Coding Assistant Instructions

## Architecture Overview

This is a **specialized drive audit repository** that tracks selective parts of a Windows C:\ drive using Git. The entire C:\ drive serves as the working directory, but only allowlisted folders are tracked through an inverse `.gitignore` pattern.

**Key Concept**: Instead of tracking a typical project structure, this repo monitors specific user folders and config directories on a Windows system while defensively excluding system files, large directories, and sensitive areas.

### Defensive Exclusion Strategy
```gitignore
# Block everything by default
/*

# Explicitly allow curated folders
!/Projects/
!/Docs/
!/Scripts/
!/Config/
!/Users/Ajpad/Documents/
!/Users/Ajpad/Desktop/

# Defense-in-depth blocking
Windows/
Program Files/
**/.git/
**/node_modules/
```

## Essential Daily Operations

### Safe Git Operations (CRITICAL)
```bash
# ALWAYS check what would be added before staging
git status --porcelain
git diff --name-only --cached
git add --dry-run .   # Preview what would be added

# Use selective staging for large changesets
git add -p    # Interactive staging
git clean -n -d      # Show what would be cleaned (never run without -n)

# Test .gitignore changes
git check-ignore -v <path>

# Verify tracking scope
git ls-files --cached --others --exclude-standard | head -20
```

### Repository Health Monitoring
```bash
# Monitor repository size and performance
git count-objects -vH && du -sh .git/

# Detect large files (>1MB) that shouldn't be tracked
git ls-files -s | awk '$3 > 1048576 {print $3/1048576 "MB", $4}' | sort -rn

# Security audit - check for credential exposure
git log --all --full-history -- "**/id_rsa*" "**/.*key*" "**/.env*"

# Find large objects in history
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | grep '^blob' | sort -nr -k3 | head -10
```

## Windows-Specific Considerations

### PowerShell Integration & File System
- **UTF-8 encoding**: `$OutputEncoding = [Text.UTF8Encoding]::UTF8` before Git operations
- **Path separators**: `.gitignore` uses both forward and backslash patterns for Windows compatibility
- **File locking**: Git operations may conflict with Windows services and applications
- **NTFS attributes**: Hidden/system file attributes can affect Git behavior unexpectedly
- **Junction points & symbolic links**: Can cause infinite loops - handle with extreme care
- **Line endings**: Mixed CRLF/LF can cause massive diffs - configure `.gitattributes` appropriately
- **PowerShell execution policy**: Consider impact when running scripts from tracked directories

### Performance & System Integration
- **Large directory scanning**: Git operations scan entire C:\ drive structure - expect delays
- **Windows Search indexer**: May compete with Git file scanning - consider exclusions
- **Network drives/UNC paths**: Can cause unexpected behavior and timeouts
- **File system watchers**: Real-time monitoring tools may interfere with Git performance
- **Antivirus software**: Real-time scanning can interfere with Git operations
- **Administrator permissions**: Some files may require elevated permissions for proper tracking

## Critical Safety Measures

### Never Do This
1. **`git add .` blindly** - Could stage system files or massive directories
2. **Modify `.gitignore` without testing** - Could expose sensitive data or system files  
3. **Ignore repository size growth** - Unintended large file tracking is expensive
4. **Work without checking disk space** - C:\ drive space affects all Git operations

### Emergency Recovery Procedures

#### If System Files Are Accidentally Staged
```bash
# Remove from staging immediately
git reset HEAD -- Windows/ "Program Files/" ProgramData/

# Verify exclusions work
git check-ignore -v Windows/System32/kernel32.dll

# If already committed (DANGEROUS - backup first)
# git filter-branch --index-filter 'git rm --cached --ignore-unmatch Windows/*' HEAD
```

#### If Repository Becomes Oversized
```bash
# Identify problem files/paths
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | grep '^blob' | sort -nr -k3

# Use git-filter-repo for cleanup (external tool required)
# git-filter-repo --path-glob '*.iso' --invert-paths
```

## Integration Points & Dependencies

- **Windows File System**: Direct NTFS permissions and file attribute integration
- **User Environment**: Tracks personal workspace and configuration drift  
- **System State**: Monitors manual changes outside version control
- **Windows Services**: May interact with files locked by running services
- **Development Tools**: IDEs and build systems may create temporary files in tracked areas

## Organizational Standards & Cross-Platform Consistency

### File & Folder Organization Principles
```
# Recommended directory structure for tracked areas
Projects/
├── Active/           # Current work projects
├── Archive/          # Completed/old projects
├── Templates/        # Project templates and boilerplates
└── Resources/        # Shared resources across projects

Docs/
├── Personal/         # Personal notes and documents
├── Reference/        # Documentation and manuals
├── Templates/        # Document templates
└── Archive/          # Old/completed documentation

Scripts/
├── PowerShell/       # Windows-specific scripts
├── Cross-Platform/   # Scripts that work on multiple OS
├── Automation/       # Scheduled/automated scripts
└── Utilities/        # One-off utility scripts

Config/
├── Applications/     # App-specific configurations
├── Development/      # IDE, editor, and dev tool configs
├── System/          # System-level configurations
└── Backups/         # Configuration backups
```

### Cross-Platform Organizational Standards
- **Use consistent naming**: `kebab-case` for folders, `PascalCase` for projects
- **Avoid platform-specific characters**: No `<>:"|?*` in filenames
- **Standardize date formats**: Use `YYYY-MM-DD` format for dated files
- **Create README.md** in each major directory explaining its purpose
- **Use consistent file extensions**: `.md` for docs, `.ps1` for PowerShell, `.sh` for Unix scripts

### Sorting & Classification Rules
```bash
# Use these patterns to maintain organization
# By project type
/Projects/Active/web-development/
/Projects/Active/data-analysis/
/Projects/Active/automation/

# By date for archives
/Projects/Archive/2024/project-name/
/Docs/Archive/2024-01/meeting-notes/

# By category for resources
/Scripts/Automation/daily-backups/
/Scripts/Utilities/file-organizers/
```

## Key Configuration Files

- **`.gitignore`** - The inverse allowlist pattern defining what gets tracked
- **`.gitattributes`** - Controls line ending handling and file type detection  
- **`CDriveRules.md`** - Documents allowlist rules and rationale (create if missing)
- **`_ORGANIZE.md`** - Organizational standards and filing rules (create for consistency)
- **Git hooks** - May contain automation specific to this unique setup
- **PowerShell scripts** - Automation tools in tracked directories

## Working Principles

**Remember**: You're working in C:\ root, not a typical project directory.

1. **Paths resolve from C:\** - Use relative paths extremely carefully
2. **Always preview changes** - Use `--dry-run` and `git status --porcelain`  
3. **Test `.gitignore` changes** - Use `git check-ignore -v <path>` before committing
4. **Regular audits** - Monitor tracked files to prevent unintended exposure
5. **Check disk space** - C:\ drive capacity affects all Git operations
6. **Run as administrator when needed** - Some system files require elevation
7. **Backup before major changes** - This setup is unique and mistakes are costly
8. **Maintain organization standards** - Use consistent naming and structure across platforms
9. **Document your filing system** - Create `_ORGANIZE.md` files to explain folder purposes

## Organizational Automation

### Recommended Scripts for File Management
```powershell
# PowerShell script to organize files by date
# Scripts/Automation/organize-by-date.ps1
Get-ChildItem "C:\Docs\Unsorted" | 
    Where-Object { $_.CreationTime -lt (Get-Date).AddDays(-30) } |
    ForEach-Object { 
        $year = $_.CreationTime.Year
        $month = $_.CreationTime.ToString("MM")
        $destPath = "C:\Docs\Archive\$year-$month"
        New-Item -ItemType Directory -Path $destPath -Force
        Move-Item $_.FullName $destPath
    }
```

### Cross-Platform File Naming Validation
```bash
# Check for problematic filenames across platforms
git ls-files | grep -E '[<>:"|?*]|[\s]$' | head -20
```

This architecture requires defensive Git practices to maintain security and performance while providing visibility into selective Windows file system changes with consistent organizational standards.