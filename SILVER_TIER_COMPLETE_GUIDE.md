# Silver Tier Testing & Submission Guide

**Complete guide for testing and submitting your AI Employee Vault Silver Tier**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Testing Your Silver Tier](#testing-your-silver-tier)
3. [Live Testing Guide](#live-testing-guide)
4. [Pytest Automated Testing](#pytest-automated-testing)
5. [Demo Video Preparation](#demo-video-preparation)
6. [GitHub Push Instructions](#github-push-instructions)
7. [Submission Checklist](#submission-checklist)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Gmail API credentials (credentials.json)
- LinkedIn access token (optional)
- Virtual environment activated

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Setup Credentials
1. Copy `.env.example` to `.env`
2. Add your Gmail and LinkedIn credentials
3. **NEVER commit .env to GitHub!**

---

## 🧪 Testing Your Silver Tier

### Test 1: File System Watcher (5 minutes)

**Start the watcher:**
```bash
python start_watcher.py
```

**Create test file:**
```bash
echo "Test file" > Inbox\test.txt
```

**Wait 30 seconds**, then check:
```bash
dir Needs_Action\action_test*.md
```

**Expected:** Action file created automatically! ✅

**Stop watcher:** Press `Ctrl+C`

---

### Test 2: Gmail Watcher (10 minutes)

**Start the watcher:**
```bash
python gmail_watcher.py
```

**Send yourself an email:**
- To: Your own email
- Subject: "Silver Tier Test"
- Mark as **Important** (star icon)
- Keep it **unread**

**Wait 5 minutes**, then check:
```bash
dir Needs_Action\EMAIL_*.md
```

**Expected:** EMAIL file created! ✅

**Stop watcher:** Press `Ctrl+C`

---

### Test 3: Approval Workflow (2 minutes)

**Create approval request:**
```bash
echo "# Test Approval

Please approve this action." > Pending_Approval\TEST_approval.md
```

**Simulate approval (manual move):**
```bash
move Pending_Approval\TEST_approval.md Approved\
move Approved\TEST_approval.md Done\
```

**Expected:** File moved through workflow! ✅

---

### Test 4: Plan.md Creation (2 minutes)

**Create a plan:**
```bash
echo "---
plan_id: test-plan-001
date_created: 2026-02-17
objective: Test plan creation
---

# Test Plan

## Objective
Test Plan.md creation functionality.

## Steps
1. Create this plan
2. Verify format
3. Confirm integration

## Timeline
- Complete by: 2026-02-17
- Priority: Normal" > Plans\PLAN_test_plan_001.md
```

**Verify format:**
```bash
type Plans\PLAN_test_plan_001.md
```

**Expected:** Proper YAML frontmatter and structure! ✅

---

### Test 5: Combined Watchers (5 minutes)

**Start all watchers:**
```bash
python run_all_watchers.py
```

**Create test file:**
```bash
echo "Combined test" > Inbox\combined.txt
```

**Wait 30 seconds**, check:
```bash
dir Needs_Action\action_combined*.md
```

**Expected:** File detected by watcher! ✅

**Stop watchers:** Press `Ctrl+C`

---

## 🧑‍💻 Live Testing Guide

### Complete Workflow Test

**Step 1:** Start file watcher
```bash
python start_watcher.py
```

**Step 2:** Create urgent task
```bash
echo "URGENT: Client needs response" > Inbox\urgent.txt
```

**Step 3:** Wait 30 seconds

**Step 4:** Check Needs_Action
```bash
dir Needs_Action\action_urgent*.md
```

**Step 5:** Create plan
```bash
echo "---
plan_id: urgent-client-001
objective: Respond to client
---

# Urgent Client Plan

## Steps
1. Review request
2. Prepare response
3. Send for approval" > Plans\PLAN_urgent_client_001.md
```

**Step 6:** Create approval
```bash
echo "# Approval Needed

Send response to client" > Pending_Approval\APPROVAL_client_001.md
```

**Step 7:** Move through workflow
```bash
move Pending_Approval\APPROVAL_client_001.md Approved\
move Approved\APPROVAL_client_001.md Done\
```

**Step 8:** Stop watcher
Press `Ctrl+C`

**Expected:** Complete workflow tested! ✅

---

## 🤖 Pytest Automated Testing

### Run All Tests
```bash
pytest test_silver_tier.py -v
```

### Expected Output
```
======================== 41 passed ========================
```

### Test Categories
- ✅ Folder Structure (7 tests)
- ✅ Core Files (5 tests)
- ✅ Documentation (5 tests)
- ✅ Skills Documentation (5 tests)
- ✅ File System Watcher (2 tests)
- ✅ Approval Workflow (2 tests)
- ✅ Plan Creation (2 tests)
- ✅ Dashboard (3 tests)
- ✅ Gmail Integration (2 tests)
- ✅ LinkedIn Integration (2 tests)
- ✅ End-to-End Workflow (1 test)
- ✅ Silver Tier Requirements (5 tests)

### Run Specific Tests
```bash
# Test folder structure only
pytest test_silver_tier.py::TestFolderStructure -v

# Test watchers only
pytest test_silver_tier.py::TestCoreFiles -v

# Test documentation
pytest test_silver_tier.py::TestDocumentationFiles -v
```

---

## 🎥 Demo Video Preparation

### What to Record (3-5 minutes)

**1. Introduction (30 seconds)**
- Show project structure
- Explain Silver Tier features
- Mention what you'll demonstrate

**2. File System Watcher (1 minute)**
- Start watcher: `python start_watcher.py`
- Create file in Inbox
- Show action file created in Needs_Action
- Explain how it works

**3. Approval Workflow (1 minute)**
- Show Pending_Approval folder
- Move file to Approved (simulate approval)
- Move file to Done (completion)
- Explain human-in-the-loop concept

**4. Plan.md Creation (30 seconds)**
- Show Plans folder
- Open a Plan.md file
- Explain YAML frontmatter and structure

**5. Dashboard (30 seconds)**
- Open Dashboard.md
- Show current status
- Explain how it tracks progress

**6. Conclusion (30 seconds)**
- Summarize features demonstrated
- Mention Silver Tier completion
- Thank reviewers

### Recording Tips
- Use screen recording software (OBS, Camtasia)
- Speak clearly and slowly
- Keep video between 3-5 minutes
- Upload to YouTube (unlisted is fine)

---

## 📤 GitHub Push Instructions

### Step 1: Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Silver Tier Complete - AI Employee Vault"
```

### Step 2: Create GitHub Repository
1. Go to github.com
2. Click "New Repository"
3. Name: `AI_Employee_Vault`
4. Make it **Public**
5. Don't initialize with README
6. Click "Create Repository"

### Step 3: Push to GitHub
```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/AI_Employee_Vault.git

# Push to GitHub
git push -u origin main
```

### ⚠️ Important Security Check

**Before pushing, verify these files are NOT included:**

```bash
# Check what will be pushed
git status

# These files should be IGNORED (not in git status):
# ❌ credentials.json
# ❌ token.json
# ❌ .env
# ❌ __pycache__/
# ❌ .venv/
# ❌ node_modules/
```

**If you see any of these in `git status`, STOP!**
- Check your `.gitignore` file
- Remove sensitive files manually

### Step 4: Verify on GitHub
1. Go to your repository on GitHub
2. Check that sensitive files are NOT there
3. Verify all code files are present
4. Check that README renders correctly

---

## ✅ Submission Checklist

### Before Submission

**Code Requirements:**
- [x] File System Watcher working
- [x] Gmail Watcher working
- [x] LinkedIn Watcher implemented
- [x] Approval workflow functional
- [x] Plan.md creation working
- [x] Dashboard updated
- [x] All tests passing (41/41)

**Documentation:**
- [x] README.md complete
- [x] Setup instructions provided
- [x] Testing guide included
- [x] Skills documented
- [x] Company handbook created

**Security:**
- [x] .gitignore configured
- [x] Credentials in .env (not committed)
- [x] No sensitive files in repository
- [x] .env.example template provided

**Submission Materials:**
- [x] GitHub repository created
- [x] Code pushed successfully
- [x] Demo video recorded (3-5 min)
- [x] Video uploaded to YouTube
- [x] Submission form ready

### Submit to Hackathon

**Form Link:** https://forms.gle/JR9T1SJq5rmQyGkGA

**Information Needed:**
1. **Tier:** Silver
2. **GitHub Repository URL:** 
   ```
   https://github.com/YOUR_USERNAME/AI_Employee_Vault
   ```
3. **Demo Video URL:**
   ```
   https://youtu.be/YOUR_VIDEO_ID
   ```
4. **Email:** Your email address
5. **Name:** Your name

### After Submission
- Keep repository public for reviewers
- Monitor email for updates
- Be ready for follow-up questions
- Start planning Gold Tier features!

---

## 🆘 Troubleshooting

### Gmail Watcher Not Working
**Problem:** No EMAIL files created

**Solution:**
1. Check credentials.json exists
2. Run `python gmail_watcher.py` to authenticate
3. Mark test email as **Important**
4. Keep test email **Unread**
5. Check internet connection

### LinkedIn Watcher Not Detecting
**Problem:** No LINKEDIN files created

**Solution:**
1. Check LINKEDIN_ACCESS_TOKEN in .env
2. Verify token is valid (not expired)
3. Check LinkedIn app permissions
4. Note: API may have rate limits

### Tests Failing
**Problem:** pytest tests failing

**Solution:**
```bash
# Run with verbose output
pytest test_silver_tier.py -v --tb=long

# Check specific error
# Fix the issue mentioned in error
# Re-run tests
```

### Git Push Failing
**Problem:** Can't push to GitHub

**Solution:**
```bash
# Check git status
git status

# If sensitive files showing:
git reset HEAD credentials.json token.json .env
git checkout -- credentials.json token.json .env

# Re-commit only safe files
git add .
git commit -m "Fixed: Removed sensitive files"
git push
```

---

## 📞 Support

**For Issues:**
1. Check this guide first
2. Review error messages carefully
3. Search for similar issues online
4. Ask for help with specific error details

**Good Question Format:**
```
I'm trying to: [what you're doing]
Expected: [what should happen]
Actual: [what actually happened]
Error: [copy full error message]
```

---

## 🎉 Congratulations!

If all tests pass and you've completed the checklist:

**Your Silver Tier is COMPLETE!** 🎊

**Next Steps:**
1. Submit to hackathon
2. Start planning Gold Tier
3. Add more features (optional)
4. Improve documentation (optional)

**Good luck with your submission!** 🚀

---

*Last Updated: 2026-02-17*
*Version: 1.0 - Silver Tier Complete*