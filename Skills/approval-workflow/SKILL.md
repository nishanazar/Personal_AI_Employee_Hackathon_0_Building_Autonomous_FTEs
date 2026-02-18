---
name: approval-workflow
description: Human-in-the-loop approval system for sensitive actions. Use when tasks require human review before execution, such as sending emails, posting on social media, or making decisions.
---

# Approval Workflow Skill

## Overview
This skill implements a human-in-the-loop approval workflow for sensitive actions. Tasks flow through: Needs_Action → Pending_Approval → Approved → Done (or Rejected). Ensures humans review important decisions before execution.

## When to Use
- Sensitive actions need human review
- Email responses require approval
- Social media posts need review
- Financial decisions need authorization
- Any action requiring human oversight

## Instructions

### Step 1: Create Approval Request
```bash
# Create file in Pending_Approval folder
echo "# Approval Request

## Action Required
Send response to client

## Details
Client requested proposal within 24 hours.

## Proposed Action
Draft response and send via email." > Pending_Approval/APPROVAL_client_response.md
```

### Step 2: Human Review
- Human reviews the approval request
- Evaluates the proposed action
- Decides to approve or reject

### Step 3: Move Based on Decision
```bash
# If APPROVED:
move Pending_Approval\file.md Approved\

# If REJECTED:
move Pending_Approval\file.md Rejected\
```

### Step 4: Execute Approved Actions
- For Approved files: Execute the action
- After completion: Move to Done folder
- Document the outcome

## Quick Start

```bash
# 1. Create approval request
echo "# Approval Needed

Action: Send email
To: client@example.com" > Pending_Approval\test.md

# 2. Review the request
type Pending_Approval\test.md

# 3. Approve (move to Approved)
move Pending_Approval\test.md Approved\

# 4. Execute action
# 5. Move to Done
move Approved\test.md Done\
```

## Examples

### Example 1: Email Approval
```yaml
Workflow:
  1. Draft email created
  2. Move to Pending_Approval
  3. Human reviews email content
  4. Move to Approved
  5. Send via MCP server
  6. Move to Done
```

### Example 2: LinkedIn Post Approval
```yaml
Workflow:
  1. LinkedIn post draft created
  2. Move to Pending_Approval
  3. Human reviews post content
  4. Move to Approved
  5. Post to LinkedIn
  6. Move to Done
```

### Example 3: Complex Decision
```yaml
Workflow:
  1. Complex task identified
  2. Plan.md created
  3. Plan submitted for approval
  4. Human approves plan
  5. Execute plan steps
  6. Mark as complete
```

## Folder Structure

```
AI_Employee_Vault/
├── Pending_Approval/    # Awaiting human review
├── Approved/            # Approved, ready to execute
├── Rejected/            # Rejected actions
└── Done/                # Completed actions
```

## Best Practices
- Always use approval for sensitive actions
- Review approval requests promptly
- Document approval decisions
- Keep approval trail for auditing
- Move files promptly after decision

## Approval Templates

### Email Approval Template
```markdown
# Approval Request: Email Send

## Recipient
to: client@example.com

## Subject
Subject: Proposal Response

## Body
[Email content here]

## Action Required
Please approve this email for sending.
```

### Social Media Post Template
```markdown
# Approval Request: LinkedIn Post

## Post Content
[Post text here]

## Hashtags
#AI #Hackathon

## Action Required
Please approve this post for publishing.
```

## Related Resources
- [Plan Creation](plan-creation.md) - Create action plans
- [MCP Email Server](mcp-email-server.md) - Send emails
- [LinkedIn Watcher](linkedin-watcher.md) - LinkedIn monitoring
- [Dashboard](dashboard.md) - Track approval status
