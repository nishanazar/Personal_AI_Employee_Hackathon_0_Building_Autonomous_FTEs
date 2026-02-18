---
name: plan-creation
description: Creates structured Plan.md files for complex tasks. Use when tasks require planning, multi-step execution, or Claude reasoning before action.
---

# Plan Creation Skill

## Overview
This skill creates structured Plan.md files for complex tasks that require careful planning and multi-step execution. Plans include objectives, steps, timelines, and success criteria.

## When to Use
- Complex tasks requiring multiple steps
- Tasks needing clear objectives and timelines
- Projects requiring documentation
- When Claude reasoning loop is needed
- Before executing important actions

## Instructions

### Step 1: Identify Need for Plan
```bash
# Triggers for plan creation:
- Complex email requiring thoughtful response
- Multi-step project
- Task with deadline
- Action requiring approval
- Project needing documentation
```

### Step 2: Create Plan.md File
```bash
# Create in Plans folder with proper structure
echo "---
plan_id: unique-id-001
date_created: 2026-02-18
status: pending_approval
objective: Clear statement of what needs to be achieved
source: Related action file if applicable
---

# Plan Title

## Objective
Clear statement of the goal.

## Steps
1. First step
2. Second step
3. Third step

## Timeline
- Start: 2026-02-18
- Complete by: 2026-02-19
- Priority: High/Normal/Low

## Resources Needed
- List any resources required

## Success Criteria
- How to measure completion
- Quality standards" > Plans\PLAN_task_001.md
```

### Step 3: Submit for Approval (if needed)
```bash
# Move to Pending_Approval for review
move Plans\PLAN_task_001.md Pending_Approval\
```

### Step 4: Execute Plan
- Follow steps in order
- Track progress
- Update status as needed

### Step 5: Mark Complete
```bash
# Update plan status
# Move to archive or keep for reference
```

## Quick Start

```bash
# Create a simple plan
echo "---
plan_id: quick-plan-001
date_created: 2026-02-18
status: pending
objective: Respond to client email
---

# Client Response Plan

## Objective
Respond to client inquiry within 24 hours.

## Steps
1. Review client email
2. Draft response
3. Submit for approval
4. Send via MCP server

## Timeline
- Complete by: 2026-02-19
- Priority: High" > Plans\PLAN_client_response.md
```

## Examples

### Example 1: Email Response Plan
```yaml
Plan ID: email-response-001
Objective: Respond to urgent client email
Steps:
  1. Review email content
  2. Research requested information
  3. Draft response
  4. Get approval
  5. Send email
Timeline: 24 hours
Priority: High
```

### Example 2: Project Plan
```yaml
Plan ID: project-alpha-001
Objective: Complete project alpha deliverables
Steps:
  1. Gather requirements
  2. Create design document
  3. Implement features
  4. Test thoroughly
  5. Deploy to production
Timeline: 2 weeks
Priority: High
Resources: Development team, testing environment
```

### Example 3: Event Planning
```yaml
Plan ID: event-webinar-001
Objective: Organize successful webinar
Steps:
  1. Choose topic and date
  2. Invite speakers
  3. Set up registration
  4. Promote event
  5. Host webinar
  6. Follow up with attendees
Timeline: 1 month
Priority: Normal
```

## Plan Template

```markdown
---
plan_id: [unique-identifier]
date_created: [YYYY-MM-DD]
status: [pending_approval | approved | in_progress | completed]
objective: [clear goal statement]
source: [related action file if applicable]
---

# [Plan Title]

## Objective
[Detailed objective statement]

## Steps
1. [First step]
2. [Second step]
3. [Third step]

## Timeline
- Start: [YYYY-MM-DD]
- Complete by: [YYYY-MM-DD]
- Priority: [High/Normal/Low]

## Resources Needed
- [Resource 1]
- [Resource 2]

## Success Criteria
- [Criterion 1]
- [Criterion 2]

## Notes
[Any additional information]
```

## Best Practices
- Use clear, actionable objectives
- Break complex tasks into small steps
- Set realistic timelines
- Define measurable success criteria
- Update plan status as progress is made
- Archive completed plans for reference

## Related Resources
- [Approval Workflow](approval-workflow.md) - Get plans approved
- [File System Watcher](file-system-watcher.md) - Detect tasks
- [Gmail Watcher](gmail-watcher.md) - Email-based planning
- [Dashboard](dashboard.md) - Track plan progress
