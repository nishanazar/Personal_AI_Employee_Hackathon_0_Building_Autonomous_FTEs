# AI Employee Vault - Silver Tier

**An intelligent file monitoring and task management system with AI-powered automation**

Built for GIAIC Hackathon 0 - **Silver Tier Complete** ✅

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Silver Tier Requirements](#silver-tier-requirements)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Documentation](#documentation)
- [Security](#security)
- [License](#license)

---

## 🎯 Overview

The AI Employee Vault is designed to monitor file changes, emails, and social media activities, then automatically create action items and follow a structured approval workflow. This system implements an automated workflow with human-in-the-loop oversight.

### Key Features
- **Multiple Watchers**: File System, Gmail, and LinkedIn monitoring
- **Automated Action Creation**: Generates action items when new items detected
- **Approval Workflow**: Human-in-the-loop for sensitive actions
- **Planning System**: Creates Plan.md files for complex tasks
- **Dashboard**: Real-time status tracking
- **Skills Documentation**: All AI functionality documented as Agent Skills

---

## ✨ Features

### Silver Tier Features

| Feature | Status | Description |
|---------|--------|-------------|
| **File System Watcher** | ✅ Complete | Monitors Inbox folder for new files |
| **Gmail Watcher** | ✅ Complete | Monitors Gmail for important emails |
| **LinkedIn Watcher** | ✅ Complete | Monitors LinkedIn for activities |
| **Plan.md Creation** | ✅ Complete | Claude reasoning loop creates plans |
| **Approval Workflow** | ✅ Complete | Human-in-the-loop approval system |
| **MCP Server** | ✅ Complete | External action capability (email) |
| **Scheduling** | ✅ Complete | Task Scheduler integration |
| **Agent Skills** | ✅ Complete | All functionality documented |

---

## 🏆 Silver Tier Requirements

All Silver Tier requirements have been completed and tested:

- ✅ **Two or More Watchers**: File System + Gmail + LinkedIn
- ✅ **LinkedIn Auto-Post**: Draft creation + approval workflow
- ✅ **Plan.md Creation**: Automated planning for complex tasks
- ✅ **MCP Server**: Email sending capability
- ✅ **Approval Workflow**: Pending → Approved → Done
- ✅ **Scheduling**: Windows Task Scheduler support
- ✅ **Agent Skills**: Complete skills documentation

**Test Results:** 41/41 pytest tests passing ✅

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Gmail API credentials (for Gmail watcher)
- LinkedIn access token (optional, for LinkedIn watcher)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd AI_Employee_Vault
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Credentials
```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and add your credentials
# NEVER commit .env to Git!
```

### 4. Run the Watchers
```bash
# Run all watchers together
python run_all_watchers.py

# Or run individually
python start_watcher.py        # File system watcher
python gmail_watcher.py        # Gmail watcher
python linkedin_watcher.py     # LinkedIn watcher
```

---

## 📦 Installation

### Python Dependencies
```bash
pip install -r requirements.txt
```

### Gmail API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Gmail API
4. Create OAuth credentials
5. Download `credentials.json`
6. Place it in the project root
7. Run `python gmail_watcher.py` once to authenticate

### LinkedIn API Setup (Optional)

1. Go to [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
2. Create a new app
3. Get your access token
4. Add to `.env` file:
   ```
   LINKEDIN_ACCESS_TOKEN=your_token_here
   ```

### MCP Email Server Setup (Optional)

```bash
cd mcp-email-server
npm install
# Edit .env with your email credentials
node index.js
```

---

## 💻 Usage

### File System Watcher

Place files in the `Inbox/` folder to trigger automatic processing:

```bash
# Create a test file
echo "Urgent task" > Inbox\urgent.txt

# Watcher will detect it within 30 seconds
# Action file created in Needs_Action/
```

### Gmail Watcher

The Gmail watcher monitors for important, unread emails:

1. Send yourself an email
2. Mark it as **Important** (star icon)
3. Keep it **Unread**
4. Watcher will detect it within 5 minutes
5. EMAIL_*.md file created in Needs_Action/

### Approval Workflow

```bash
# 1. Action file appears in Needs_Action/
# 2. Move to Pending_Approval/ for review
move Needs_Action\action.md Pending_Approval\

# 3. Review and move to Approved/
move Pending_Approval\action.md Approved\

# 4. Complete and move to Done/
move Approved\action.md Done\
```

### Plan.md Creation

For complex tasks, create a Plan.md file:

```bash
echo "---
plan_id: my-plan-001
date_created: 2026-02-17
objective: My goal
---

# My Plan

## Objective
What I want to achieve

## Steps
1. Step 1
2. Step 2

## Timeline
- Complete by: 2026-02-17
- Priority: Normal" > Plans\PLAN_my_plan_001.md
```

---

## 📁 Project Structure

```
AI_Employee_Vault/
├── .env                  # Your credentials (DO NOT COMMIT!)
├── .env.example          # Template for .env
├── .gitignore            # Git ignore rules
├── base_watcher.py       # Base watcher class
├── file_system_watcher.py
├── gmail_watcher.py
├── linkedin_watcher.py
├── run_all_watchers.py
├── start_watcher.py
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── Dashboard.md          # Real-time status
├── Company_Handbook.md   # Rules and guidelines
├── Inbox/                # Place files here to trigger watcher
├── Needs_Action/         # Auto-generated action files
├── Pending_Approval/     # Files awaiting approval
├── Approved/             # Approved files
├── Rejected/             # Rejected files
├── Done/                 # Completed tasks
├── Plans/                # Plan.md files
├── Skills/               # Skills documentation
└── mcp-email-server/     # MCP email server
```

---

## 🧪 Testing

### Run All Tests
```bash
pytest test_silver_tier.py -v
```

### Expected Output
```
======================== 41 passed ========================
```

### Test Categories
- Folder Structure (7 tests)
- Core Files (5 tests)
- Documentation (5 tests)
- Skills Documentation (5 tests)
- File System Watcher (2 tests)
- Approval Workflow (2 tests)
- Plan Creation (2 tests)
- Dashboard (3 tests)
- Gmail Integration (2 tests)
- LinkedIn Integration (2 tests)
- End-to-End Workflow (1 test)
- Silver Tier Requirements (5 tests)

### Manual Testing
See `SILVER_TIER_COMPLETE_GUIDE.md` for detailed manual testing instructions.

---

## 📚 Documentation

### Main Documentation
- `README.md` - This file (project overview)
- `Dashboard.md` - Real-time status and counts
- `Company_Handbook.md` - Rules and guidelines

### Guides
- `SILVER_TIER_COMPLETE_GUIDE.md` - Complete testing and submission guide

### Skills Documentation
- `Skills/all_silver_skills_documentation.md` - All skills overview
- `Skills/Watchers/gmail_setup_guide.md` - Gmail API setup
- `Skills/Watchers/linkedin_setup_guide.md` - LinkedIn API setup
- `Skills/Scheduling/task_scheduler_silver.md` - Task Scheduler setup
- `Skills/MCP/mcp_email_server_guide.md` - MCP server setup

---

## 🔒 Security

### Important Security Notes

**NEVER commit these files to GitHub:**
- ❌ `credentials.json` - Gmail API credentials
- ❌ `token.json` - Gmail OAuth token
- ❌ `.env` - Your environment variables
- ❌ `*.key`, `*.pem` - Private keys

**Always keep these private:**
- API credentials
- Access tokens
- Passwords
- Private keys

### .gitignore Configuration

This project includes a `.gitignore` file that automatically excludes:
- Credentials and tokens
- Virtual environments
- Node modules
- Cache files
- Test data


## 📄 License

This project is open source and available under the MIT License.

---

## 🎉 Acknowledgments

Built for **GIAIC Hackathon 0** - Silver Tier

**Features Implemented:**
- Multiple watchers (File System, Gmail, LinkedIn)
- Automated action creation
- Human-in-the-loop approval workflow
- Plan.md generation
- MCP server integration
- Task scheduling
- Comprehensive skills documentation

**Test Results:** 41/41 tests passing ✅

---

*Last Updated: 2026-02-17*  
*Version: 1.0 - Silver Tier Complete*