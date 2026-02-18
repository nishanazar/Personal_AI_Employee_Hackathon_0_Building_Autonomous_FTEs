import subprocess
import sys
import os
from pathlib import Path

def main():
    """
    Script to run all watchers simultaneously
    This allows both filesystem and gmail watchers to run at the same time
    """
    vault_path = Path(__file__).parent
    os.chdir(vault_path)  # Change to the vault directory
    
    print("Starting all watchers...")
    
    try:
        # Start the filesystem watcher
        fs_process = subprocess.Popen([sys.executable, "filesystem_watcher.py"])
        print(f"Started filesystem watcher with PID: {fs_process.pid}")
        
        # Start the gmail watcher
        gmail_process = subprocess.Popen([sys.executable, "gmail_watcher.py"])
        print(f"Started gmail watcher with PID: {gmail_process.pid}")
        
        print("Both watchers are now running!")
        print("Press Ctrl+C to stop all watchers.")
        
        # Wait for both processes to complete (they won't unless interrupted)
        fs_process.wait()
        gmail_process.wait()
        
    except KeyboardInterrupt:
        print("\nStopping all watchers...")
        print("Watchers stopped successfully.")

if __name__ == "__main__":
    main()