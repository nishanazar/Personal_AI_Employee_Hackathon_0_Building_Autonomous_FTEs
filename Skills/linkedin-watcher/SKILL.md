---
name: linkedin-watcher
description: Monitors LinkedIn for messages, posts, and activities. Use when LinkedIn monitoring is needed or when social media activities should trigger automated workflows.
---

# LinkedIn Watcher Skill

## Overview
This skill monitors your LinkedIn account for new messages, posts, comments, and other activities. It integrates with LinkedIn API to fetch activities every 10 minutes and creates structured action items.

## When to Use
- You want to monitor LinkedIn for messages or activities
- Social media engagement needs tracking
- LinkedIn messages should create action items
- You need automated LinkedIn response workflows

## Instructions

### Step 1: Setup LinkedIn API
```bash
# 1. Go to LinkedIn Developer Portal
# 2. Create app at: https://www.linkedin.com/developers/apps
# 3. Get verified (requires business verification)
# 4. Generate access token
# 5. Add to .env file
```

### Step 2: Configure Token
```bash
# In .env file:
LINKEDIN_ACCESS_TOKEN=your_access_token_here
LINKEDIN_CLIENT_ID=your_client_id_here
```

### Step 3: Start LinkedIn Watcher
```bash
# Start watcher (checks every 10 minutes)
python linkedin_watcher.py
```

### Step 4: Monitor Activities
- Watcher checks for new messages, posts, comments
- Creates LINKEDIN_*.md files in Needs_Action
- Includes activity metadata and content

## Quick Start

```bash
# 1. Add token to .env file
# 2. Start watcher
python linkedin_watcher.py

# 3. Send/receive LinkedIn message
# 4. Wait 10 minutes
# 5. Check Needs_Action for LINKEDIN_*.md files
```

## Examples

### Example 1: Message Detection
```yaml
Input:
  - Receive LinkedIn message
  - Or send message to yourself

Output:
  - File: LINKEDIN_message_20260218_120000.md
  - Contains: Sender, content, timestamp, conversation ID
```

### Example 2: Post Engagement
```yaml
Input:
  - Someone comments on your post

Output:
  - File: LINKEDIN_comment_20260218_120000.md
  - Action: Consider responding to comment
```

## Configuration

### Environment Variables (.env)
```bash
LINKEDIN_ACCESS_TOKEN=your_token_here
LINKEDIN_CLIENT_ID=your_client_id
```

### Watcher Settings
```python
check_interval = 600  # Check every 10 minutes
```

## API Scopes Required
- `w_member_social` - Create/modify posts
- `r_profile_basicinfo` - Access profile info
- `r_messages` - Read messages (requires special approval)
- `email` - Access email address
- `openid` - Authentication

## Best Practices
- Keep LinkedIn token secure (never commit)
- Respect rate limits (10-minute intervals)
- Use for professional engagement tracking
- Respond to important messages promptly
- Archive processed activities

## Security
- Never commit .env file with tokens
- Store LinkedIn credentials securely
- Rotate tokens periodically
- Monitor API usage for unusual activity

## Troubleshooting

### Invalid Token Error
- Generate new token from LinkedIn Developer Portal
- Update .env file with new token
- Wait 5-10 minutes for activation
- Verify app is verified/published

### No Activities Detected
- Check if r_messages scope is approved
- Verify LinkedIn app has proper permissions
- Check API rate limits
- Ensure internet connection

### API Restrictions
- LinkedIn has strict API policies
- Some endpoints require business verification
- Messaging API needs special approval
- Personal use may have limitations

## Related Resources
- [File System Watcher](file-system-watcher.md) - Monitor files
- [Gmail Watcher](gmail-watcher.md) - Monitor emails
- [Approval Workflow](approval-workflow.md) - Approval process
- [Plan Creation](plan-creation.md) - Create action plans
