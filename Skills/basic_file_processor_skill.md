---
skill_id: bronze-file-drop-processor
name: Basic File Drop Processor
description: Handles files dropped by filesystem watcher into Needs_Action
tier: Bronze
version: 0.1

When triggered:
- Scan Needs_Action for new .md files
- Read file metadata (type, original_name, size)
- Add processing note to the file
- Move file to Done folder
- Update Dashboard.md with entry under Real-time Summary: "- Processed: [original_name] on [date]"

Trigger phrase: "process pending drops"

Use file system tools to implement.
---