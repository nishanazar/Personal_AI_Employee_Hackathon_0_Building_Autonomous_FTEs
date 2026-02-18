---
name: mcp-email-server
description: MCP (Model Context Protocol) server for sending emails via external action. Use when emails need to be sent programmatically or when external email actions are required.
---

# MCP Email Server Skill

## Overview
This skill provides MCP server functionality for sending emails via Node.js. It enables the AI Employee Vault to send real emails through Gmail SMTP or other email providers.

## When to Use
- You need to send emails programmatically
- Email responses need to be sent automatically
- External email action is required
- Integration with email providers is needed
- Automated email notifications are needed

## Instructions

### Step 1: Setup MCP Email Server
```bash
# Navigate to MCP server directory
cd mcp-email-server

# Install dependencies
npm install nodemailer
```

### Step 2: Configure Email Credentials
```javascript
// index.js configuration
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'your_email@gmail.com',
    pass: 'your_app_password'  // Gmail App Password
  }
});
```

### Step 3: Start MCP Server
```bash
# Start the server
node index.js

# Server runs on port 3000
```

### Step 4: Send Email via MCP
```javascript
// POST request to send email
POST http://localhost:3000/send-email
Content-Type: application/json

{
  "to": "recipient@example.com",
  "subject": "Email Subject",
  "text": "Email body content"
}
```

### Step 5: Verify Email Sent
- Check email sent confirmation
- Verify recipient received email
- Move approval file to Done folder

## Quick Start

```bash
# 1. Setup server
cd mcp-email-server
npm install

# 2. Configure credentials
# Edit index.js with your Gmail credentials

# 3. Start server
node index.js

# 4. Test email sending
# Use Postman or curl to send test email
curl -X POST http://localhost:3000/send-email \
  -H "Content-Type: application/json" \
  -d '{"to":"test@example.com","subject":"Test","text":"Test email"}'
```

## Examples

### Example 1: Send Client Response
```yaml
Input:
  - Approved email in Approved folder
  - Email details: to, subject, body

Process:
  1. Read email from Approved folder
  2. POST to MCP server
  3. Verify email sent
  4. Move file to Done

Output:
  - Email sent successfully
  - File moved to Done folder
```

### Example 2: Automated Notification
```yaml
Input:
  - Task completion detected
  - Need to notify stakeholder

Process:
  1. Create email notification
  2. Submit for approval
  3. Send via MCP server
  4. Log notification

Output:
  - Stakeholder notified
  - Notification logged
```

## Configuration

### Gmail Setup
```javascript
{
  service: 'gmail',
  auth: {
    user: 'your_email@gmail.com',
    pass: 'your_16_char_app_password'
  }
}
```

### Gmail App Password Setup
1. Go to Google Account Settings
2. Enable 2-Factor Authentication
3. Generate App Password
4. Use 16-character password in config

### Server Configuration
```javascript
// index.js
const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/send-email', (req, res) => {
  const { to, subject, text } = req.body;
  // Send email logic
});

app.listen(PORT, () => {
  console.log(`MCP Email Server running on port ${PORT}`);
});
```

## Best Practices
- Never commit email credentials to Git
- Use environment variables for credentials
- Implement error handling
- Log all sent emails
- Rate limit email sending
- Validate email addresses before sending

## Security
- Use Gmail App Passwords (not regular password)
- Enable 2FA on email account
- Store credentials in .env file
- Never expose credentials in code
- Implement rate limiting
- Validate all email inputs

## Troubleshooting

### Server Won't Start
- Check if port 3000 is available
- Verify Node.js is installed
- Check for syntax errors in index.js
- Ensure nodemailer is installed

### Email Not Sending
- Verify Gmail credentials are correct
- Check Gmail App Password is valid
- Ensure 2FA is enabled
- Check internet connection
- Verify recipient email address

### Authentication Error
- Regenerate Gmail App Password
- Update credentials in index.js
- Restart MCP server
- Check Gmail account settings

## Related Resources
- [Approval Workflow](approval-workflow.md) - Approve emails before sending
- [Gmail Watcher](gmail-watcher.md) - Receive emails
- [Plan Creation](plan-creation.md) - Plan email campaigns
- [Dashboard](dashboard.md) - Track sent emails
