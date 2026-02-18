---
title: Gmail Watcher Real Setup Guide – Silver Tier Step 9
date: 2026-02-13
status: in_progress
---

## Step-by-Step Gmail Watcher Setup

1. Google Cloud Console jaao:
   https://console.cloud.google.com/
   Naya project banao (naam: AI-Employee-Hackathon)

2. APIs & Services → Library → "Gmail API" search karo → Enable karo

3. Credentials → Create Credentials → OAuth client ID
   - Application type: Desktop app
   - Name: Gmail Watcher Client
   - Download JSON file → naam rakho: credentials.json
   - Is file ko safe jagah rakho (Broze folder mein .gitignore ke saath)

4. Python libraries install (terminal mein Broze folder se):
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

5. gmail_watcher.py file banani hai (skeleton below)

## gmail_watcher.py Skeleton (copy this to real file later)

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from base_watcher import BaseWatcher  # assume base_watcher.py exists
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

class GmailWatcher(BaseWatcher):
    def __init__(self, vault_path: str):
        super().__init__(vault_path, check_interval=300)  # 5 min
        self.creds = None
        self.service = None
        self._authenticate()

    def _authenticate(self):
        creds_file = 'credentials.json'
        token_file = 'token.json'
        if os.path.exists(token_file):
            self.creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        if not self.creds or not self.creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            self.creds = flow.run_local_server(port=0)
            with open(token_file, 'w') as token:
                token.write(self.creds.to_json())
        self.service = build('gmail', 'v1', credentials=self.creds)

    def check_for_updates(self):
        # Yeh real mein emails fetch karega
        # Abhi sirf print kar rahe hain
        print("Checking Gmail for new important emails...")
        return []  # placeholder

# Run test: if __name__ == "__main__": watcher = GmailWatcher(vault_path); watcher.run()

Next real action: credentials.json banao aur test run karo