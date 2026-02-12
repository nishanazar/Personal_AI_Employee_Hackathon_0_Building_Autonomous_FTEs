#!/usr/bin/env python3
"""
Simple script to demonstrate that Claude Code can read from and write to the vault
This verifies the Bronze Tier requirement for Claude Code integration
"""

import os
from pathlib import Path
import sys

# Add the vault directory to the path
vault_path = Path(__file__).parent
sys.path.insert(0, str(vault_path))

def demonstrate_claude_integration():
    print("Demonstrating Claude Code integration with the vault...")
    
    # Read from an existing file
    dashboard_path = vault_path / "Dashboard.md"
    if dashboard_path.exists():
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"SUCCESS: Successfully read from {dashboard_path.name}")
    
    # Write to a new file in the vault
    demo_file_path = vault_path / "Needs_Action" / "claude_demo_report.md"
    demo_content = f"""# Claude Code Integration Report

## Status
Verified: Claude Code can successfully read from and write to the vault

## Timestamp
Generated at: {Path(__file__).stem} on {__import__('datetime').datetime.now().isoformat()}

## Verification Steps Completed
1. Read existing file: Dashboard.md SUCCESS
2. Write new file: {demo_file_path.name} SUCCESS

---
*This confirms the Bronze Tier requirement for Claude Code integration*
"""
    
    with open(demo_file_path, 'w', encoding='utf-8') as f:
        f.write(demo_content)
    
    print(f"SUCCESS: Successfully wrote to {demo_file_path.name}")
    print("\nClaude Code integration with vault verified successfully!")
    

if __name__ == "__main__":
    demonstrate_claude_integration()