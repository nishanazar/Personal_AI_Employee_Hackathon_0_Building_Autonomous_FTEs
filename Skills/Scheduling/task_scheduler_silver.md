---
title: Task Scheduler Setup - Silver Tier Auto-Run
date: 2026-02-14
status: completed
---

## Goal
Watchers aur Claude processing ko automatic banao (laptop restart pe bhi chalte rahein)

## Windows Task Scheduler Steps
1. Windows search mein "Task Scheduler" kholo
2. Right side → Create Basic Task
3. Name: "AI Employee - Gmail Watcher"
4. Trigger: Daily → Start time: 8:00 AM (ya har ghante test ke liye)
5. Action: Start a program
   - Program/script: C:\Users\USER\hackthon_0\Broze\.venv\Scripts\python.exe
   - Arguments: gmail_watcher.py
6. Dusra task banao: "AI Employee - File Watcher"
   - Same tareeqe se filesystem_watcher.py ke liye
7. Teesra task (optional): Claude prompt daily run
   - Arguments: "run silver processing" (Claude CLI command)

## Test Karne Ka Tareeqa
- Task pe right-click → Run → terminal khulna chahiye
- Laptop restart karo → 5-10 min baad Needs_Action mein file aati hai ya nahi check karo

## Security
- Tasks ko "Run whether user is logged on or not" select karo
- Password maangega → daal do