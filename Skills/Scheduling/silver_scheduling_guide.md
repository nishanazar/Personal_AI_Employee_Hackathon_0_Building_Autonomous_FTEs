---
title: Silver Tier Scheduling Setup - Step 11
date: 2026-02-13
status: in_progress
---

## Goal
Make watchers and Claude processing automatic (no manual run every time)

## Option 1: Windows Task Scheduler (recommended for Windows)
1. Open Task Scheduler (Windows search mein "Task Scheduler" type karo)
2. Right side → Create Basic Task
3. Name: "AI Employee Watchers & Processing"
4. Trigger: Daily → Start time: 8:00 AM (ya har ghante)
5. Action: Start a program
   - Program/script: C:\Users\USER\hackthon_0\Broze\.venv\Scripts\python.exe
   - Add arguments: gmail_watcher.py   (ya filesystem_watcher.py)
6. Multiple tasks bana sakti ho:
   - Task 1: Gmail watcher (har 15 min)
   - Task 2: Claude prompt run (har ghante: "run silver processing")

## Option 2: Run both watchers together (simple script)
Create run_all_watchers.py in Broze folder:
import subprocess
subprocess.Popen(["python", "filesystem_watcher.py"])
subprocess.Popen(["python", "gmail_watcher.py"])
print("Both watchers started!")

Then schedule this script in Task Scheduler.

## Next
- Create Task Scheduler tasks
- Test auto-run after laptop restart