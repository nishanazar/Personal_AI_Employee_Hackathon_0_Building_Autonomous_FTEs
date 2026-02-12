#!/usr/bin/env python3
"""
File System Watcher Starter Script
This script starts the file system watcher to monitor the Inbox folder.
"""

import sys
import os
from pathlib import Path

# Add the vault directory to the path so we can import the watcher modules
vault_path = Path(__file__).parent
sys.path.insert(0, str(vault_path))

from file_system_watcher import FileSystemWatcher

def main():
    print("Starting File System Watcher...")
    print(f"Monitoring vault: {vault_path}")
    print("Press Ctrl+C to stop the watcher.")

    # Create and start the file system watcher
    # It will monitor the Inbox folder and check every 30 seconds
    watcher = FileSystemWatcher(
        vault_path=str(vault_path),
        watch_folder="Inbox",
        check_interval=30
    )

    try:
        watcher.run()
    except KeyboardInterrupt:
        print("\nStopping File System Watcher...")
        print("Watcher stopped successfully.")

if __name__ == "__main__":
    main()