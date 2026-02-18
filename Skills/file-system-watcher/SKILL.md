---
name: file-system-watcher
description: Monitors the Inbox folder for new files and automatically creates action items in Needs_Action. Use when files are added to the Inbox or when automatic file processing is needed.
---

# File System Watcher Skill

## Overview
This skill monitors the Inbox folder for new files and automatically creates structured action items in the Needs_Action folder. It's the core automation component of the AI Employee Vault system.

## When to Use
- New files are placed in the Inbox folder
- Automatic file processing is required
- You want to track file-based tasks automatically
- Files need to be converted into actionable items

## Instructions

### Step 1: Start the Watcher
```bash
# Start the file system watcher
python start_watcher.py

# Or run all watchers together
python run_all_watchers.py
```

### Step 2: Place Files in Inbox
```bash
# Any file placed here will be detected
echo "Task content" > Inbox/task.txt
```

### Step 3: Watcher Automatically Creates Action File
The watcher will:
- Detect the new file within 30 seconds
- Create an action file in Needs_Action folder
- Include file metadata and content preview
- Add processing instructions

### Step 4: Process the Action File
- Review the action file in Needs_Action
- Take appropriate action
- Move through approval workflow if needed
- Move to Done when complete

## Quick Start

```bash
# 1. Start watcher
python start_watcher.py

# 2. Create test file
echo "Test task" > Inbox/test.txt

# 3. Wait 30 seconds

# 4. Check Needs_Action folder
dir Needs_Action\action_test*.md
```

## Examples

### Example 1: Basic File Detection
```bash
# Input: Place file in Inbox
echo "Meeting notes from client call" > Inbox/meeting_notes.txt

# Output: Action file created in Needs_Action
# File: action_meeting_notes_20260218_120000.md
# Contains: File info, content preview, action required
```

### Example 2: Complex Task Processing
```bash
# Input: Complex task file
echo "URGENT: Client needs proposal within 24 hours" > Inbox/urgent_proposal.txt

# Output: Action file with urgency flag
# File: action_urgent_proposal_20260218_120000.md
# Next: Create Plan.md, submit for approval
```

## Best Practices
- Keep Inbox folder clean - only add files ready for processing
- Check Needs_Action folder regularly for new action items
- Use descriptive filenames for easier tracking
- Move completed actions to Done folder promptly
- Use approval workflow for sensitive actions

## Configuration

### Watcher Settings (start_watcher.py)
```python
watch_folder = "Inbox"        # Folder to monitor
check_interval = 30           # Check every 30 seconds
```

### Customization
- Change check interval for faster/slower detection
- Monitor different folders by modifying watch_folder
- Add custom action file templates

## Related Resources
- [Gmail Watcher](gmail-watcher.md) - Monitor Gmail for emails
- [LinkedIn Watcher](linkedin-watcher.md) - Monitor LinkedIn activities
- [Approval Workflow](approval-workflow.md) - Human-in-the-loop approval process
- [Plan Creation](plan-creation.md) - Create structured plans for complex tasks

## Troubleshooting

### Watcher Not Detecting Files
- Check if watcher is running: `tasklist | findstr python`
- Verify Inbox folder exists and has correct path
- Check file permissions
- Restart watcher if needed

### Action Files Not Created
- Check Needs_Action folder permissions
- Verify watcher didn't crash (check console output)
- Ensure file isn't already processed (watcher tracks processed files)
