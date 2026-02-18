---
title: Gmail Watcher Setup Complete - Silver Tier Step 10
date: 2026-02-13
status: completed
---

## Gmail Watcher Setup Summary

- Google Cloud project: abcd (ID: gen-lang-client-0609739168)
- Gmail API: Enabled
- OAuth Client: Desktop app created
- credentials.json: Downloaded and placed in C:\Users\USER\hackthon_0\Broze
- Libraries installed: google-api-python-client, google-auth-httplib2, google-auth-oauthlib
- Script: gmail_watcher.py ready in Broze folder
- First run: Browser login + permission done
- Token saved: token.pickle file created

## How to run Gmail watcher
cd C:\Users\USER\hackthon_0\Broze
python gmail_watcher.py

- Watches every 5 minutes
- Creates .md files in Needs_Action for unread important emails
- Test: Send yourself an email with "urgent" in subject

## Next actions
- Test with real email
- Add scheduling (Task Scheduler)
- Integrate with Plan.md creation prompt