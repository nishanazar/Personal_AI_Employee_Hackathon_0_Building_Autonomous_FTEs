---
name: dashboard
description: Real-time status tracking and monitoring dashboard. Use when you need to check system status, view task counts, or monitor overall AI Employee Vault health.
---

# Dashboard Skill

## Overview
This skill maintains and updates the Dashboard.md file which provides real-time visibility into the AI Employee Vault system status, task counts, and overall health.

## When to Use
- You need to check current system status
- Want to see task counts at a glance
- Monitoring system health
- Reporting progress to stakeholders
- Tracking completed vs pending tasks

## Instructions

### Step 1: View Dashboard
```bash
# Open Dashboard.md to see current status
type Dashboard.md
```

### Step 2: Understand Dashboard Sections

#### Real-time Summary
- Current tasks in progress
- Completed tasks today
- Pending approvals count
- Watcher status

#### Tier Status
- Bronze Tier milestone (completed)
- Silver Tier status (complete/in-progress)
- Features active checklist

#### Current System Status
- File System Watcher: Running/Stopped
- Gmail Watcher: Running/Stopped
- LinkedIn Watcher: Running/Stopped
- Approval Workflow: Active/Inactive

### Step 3: Update Dashboard (Manual)
```bash
# Edit Dashboard.md to update counts
# Update task counts based on folder contents
# Update watcher status
```

### Step 4: Update Dashboard (Automatic)
```python
# Run dashboard update script
python update_dashboard.py
```

## Quick Start

```bash
# 1. Check current dashboard
type Dashboard.md

# 2. Count files in each folder
dir /b Inbox | find /c ".md"
dir /b Needs_Action | find /c ".md"
dir /b Pending_Approval | find /c ".md"
dir /b Done | find /c ".md"

# 3. Update dashboard with counts
# Edit Dashboard.md manually or run update script
```

## Examples

### Example 1: Daily Status Check
```markdown
## Real-time Summary
- Current tasks in progress: 5
- Completed tasks today: 3
- Pending approvals: 2
- Watcher check: All watchers active (2026-02-18)
```

### Example 2: Silver Tier Status
```markdown
## Silver Tier Status: ✅ COMPLETE
- ✅ Two watchers running: File system + Gmail
- ✅ Plan.md creation working
- ✅ Approval workflow tested
- ✅ Email draft generation tested
- ✅ Scheduling setup complete
```

### Example 3: System Health
```markdown
## Current System Status
- File System Watcher: ✅ Running (checking every 30s)
- Gmail Watcher: ✅ Running (checking every 5m)
- LinkedIn Watcher: ✅ Running (checking every 10m)
- Approval Workflow: ✅ Active
- Dashboard: ✅ Updated in real-time
```

## Dashboard Template

```markdown
# Dashboard

## Real-time Summary
- Current tasks in progress: [count from Needs_Action + Pending_Approval]
- Completed tasks today: [count from Done created today]
- Pending approvals: [count from Pending_Approval]
- Inbox items: [count from Inbox]
- Watcher check: [status and timestamp]

## Silver Tier Status
- Status: COMPLETE / IN PROGRESS
- Features Active: [list of working features]

## Current System Status
- File System Watcher: [status]
- Gmail Watcher: [status]
- LinkedIn Watcher: [status]
- Approval Workflow: [status]

## Completion Checklist
- [x] Two or more watchers
- [x] Plan.md creation working
- [x] Approval workflow tested
- [x] Email draft generation tested
- [x] Scheduling setup complete
```

## Best Practices
- Update dashboard regularly (at least daily)
- Keep counts accurate and current
- Use clear status indicators (✅/❌)
- Include timestamps for last update
- Archive old dashboard versions

## Automation

### Auto-Update Script
```python
# update_dashboard.py
from pathlib import Path

vault = Path('.')
inbox = len(list(vault.glob('Inbox/*')))
needs_action = len(list(vault.glob('Needs_Action/*.md')))
pending = len(list(vault.glob('Pending_Approval/*.md')))
done = len(list(vault.glob('Done/*.md')))

# Update Dashboard.md with counts
```

## Related Resources
- [File System Watcher](file-system-watcher.md) - Check watcher status
- [Gmail Watcher](gmail-watcher.md) - Email monitoring status
- [LinkedIn Watcher](linkedin-watcher.md) - LinkedIn monitoring status
- [All Skills Documentation](all_silver_skills_documentation.md) - Complete skills overview
