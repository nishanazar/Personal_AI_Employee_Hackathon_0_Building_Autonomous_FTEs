---
name: gmail-watcher
description: Monitors Gmail for important unread emails and automatically creates action items. Use when email monitoring is needed or when important emails should trigger automated workflows.
---

# Gmail Watcher Skill

## Overview
This skill monitors your Gmail account for important, unread emails and automatically creates structured action items in the Needs_Action folder. It integrates with Gmail API to fetch emails every 5 minutes.

## When to Use
- You want to monitor Gmail for important emails
- Email-based task automation is needed
- Important emails should create action items automatically
- You need email-to-task conversion

## Instructions

### Step 1: Setup Gmail API Credentials
```bash
# 1. Go to Google Cloud Console
# 2. Create project and enable Gmail API
# 3. Download credentials.json
# 4. Place in project root
# 5. Run watcher once to authenticate
python gmail_watcher.py
```

### Step 2: Start Gmail Watcher
```bash
# Start Gmail watcher (checks every 5 minutes)
python gmail_watcher.py
```

### Step 3: Mark Emails as Important
- Gmail watcher only fetches emails marked as **Important**
- Keep important emails **Unread** until processed
- Watcher will detect and create EMAIL_*.md files

### Step 4: Process Email Action Files
- Review EMAIL_*.md files in Needs_Action
- Extract email content and metadata
- Create response drafts if needed
- Move through approval workflow

## Quick Start

```bash
# 1. Ensure credentials.json exists
# 2. Start watcher
python gmail_watcher.py

# 3. Send yourself an important email
# 4. Wait 5 minutes
# 5. Check Needs_Action for EMAIL_*.md files
```

## Examples

### Example 1: Email Detection
```yaml
Input: 
  - Send email to yourself
  - Mark as Important (star)
  - Keep unread

Output:
  - File: EMAIL_Subject_20260218_120000.md
  - Location: Needs_Action/
  - Contains: Sender, subject, snippet, full metadata
```

### Example 2: Email Response Workflow
```yaml
Input: Client email requesting proposal
Process:
  1. Gmail watcher detects email
  2. Creates EMAIL_client_proposal.md
  3. Create Plan.md for response
  4. Draft response email
  5. Submit for approval
  6. Send via MCP server
```

## Configuration

### Environment Variables (.env)
```bash
GMAIL_CREDENTIALS_FILE=credentials.json
GMAIL_TOKEN_FILE=token.json
```

### Watcher Settings
```python
check_interval = 300  # Check every 5 minutes
query = 'is:unread is:important newer_than:1d'
```

## Best Practices
- Only mark truly important emails as important
- Process emails promptly to keep inbox clean
- Use approval workflow for email responses
- Archive processed emails to avoid re-processing
- Keep credentials.json secure (never commit to Git)

## Security
- Never commit credentials.json or token.json to Git
- Store credentials in secure location
- Use .env file for sensitive configuration
- Rotate credentials periodically

## Troubleshooting

### Authentication Error
- Run `python gmail_watcher.py` to re-authenticate
- Check credentials.json exists
- Verify Gmail API is enabled in Google Cloud Console
- Check token.json is valid

### No Emails Detected
- Ensure emails are marked as Important
- Keep emails Unread
- Check Gmail API quota limits
- Verify internet connection

## Related Resources
- [File System Watcher](file-system-watcher.md) - Monitor file system
- [LinkedIn Watcher](linkedin-watcher.md) - Monitor LinkedIn
- [MCP Email Server](mcp-email-server.md) - Send emails via MCP
- [Approval Workflow](approval-workflow.md) - Approval process
