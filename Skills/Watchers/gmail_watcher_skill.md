---
skill_name: Gmail Watcher Skill
tier: Silver
description: Monitors Gmail for new important/unread emails and creates .md files in Needs_Action
status: planning_phase
---

## How this skill should work (planned)

- Every 5-15 minutes check Gmail (using Google API)
- Look for: is:unread label:important OR "hackathon" OR "urgent" in subject/body
- For each new email:
  - Create file: Needs_Action/EMAIL_[message_id].md
  - Frontmatter:
    type: email
    from: sender
    subject: ...
    received: ...
    priority: high/medium/low
  - Body: snippet + full headers if possible
- Mark email as read or add label "processed-by-ai" (future)

## Next actions needed
- Setup Google Cloud project + enable Gmail API
- Create OAuth credentials (desktop app)
- Install google-api-python-client, google-auth-oauthlib
- Write gmail_watcher.py based on base_watcher.py pattern