# LinkedIn API Setup Guide for Silver Tier

## Overview
This guide will help you set up LinkedIn API access for your LinkedIn watcher.

## Prerequisites
- A LinkedIn account
- A company page or personal account with developer access

## Step 1: Create a LinkedIn Developer Account
1. Go to [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
2. Sign in with your LinkedIn account
3. Click on "Create App"

## Step 2: Create a LinkedIn Application
1. On the "My Apps" page, click "Create App"
2. Fill in the application details:
   - Application name: "AI Employee LinkedIn Watcher"
   - Application description: "LinkedIn watcher for AI Employee Vault"
   - Website URL: You can use a placeholder like https://example.com
   - Logo: Upload a logo (optional)
3. Accept the terms and conditions
4. Click "Create Application"

## Step 3: Configure Application Settings
1. In your application dashboard, go to "Products"
2. Apply for the "Marketing Developer Platform" or "Sign In with LinkedIn"
3. For basic monitoring, you'll need permissions like:
   - r_liteprofile (Basic profile information)
   - r_emailaddress (Email address)
   - w_member_social (Share with your network)

## Step 4: Get API Credentials
1. Go to the "Auth" tab in your application
2. Note down your:
   - Client ID
   - Client Secret

## Step 5: Generate Access Token
1. You'll need to generate an access token for your application
2. Use the OAuth 2.0 flow to get a long-lived access token
3. The basic flow involves:
   - Redirecting user to authorization URL
   - Getting authorization code
   - Exchanging code for access token

## Step 6: Set Environment Variable
1. Set the access token as an environment variable:
   ```bash
   # On Windows Command Prompt
   set LINKEDIN_ACCESS_TOKEN=your_access_token_here
   
   # On Windows PowerShell
   $env:LINKEDIN_ACCESS_TOKEN="your_access_token_here"
   
   # Permanently set in system:
   # System Properties → Advanced → Environment Variables → Add LINKEDIN_ACCESS_TOKEN
   ```

## Step 7: Test the LinkedIn Watcher
1. Run the LinkedIn watcher:
   ```bash
   python linkedin_watcher.py
   ```
2. The watcher will start monitoring your LinkedIn account for new activities

## Important Notes
- LinkedIn's API has strict rate limits
- Some endpoints require LinkedIn's approval
- For Silver Tier, you can simulate the functionality even without full API access
- The code structure is ready to work once you have proper API access

## Alternative: LinkedIn Notifications Simulation
If you can't get full API access for Silver Tier, you can create a simple notification checker that periodically checks for LinkedIn notifications using web scraping (with proper permissions) or create a manual process where you copy-paste notifications to trigger the workflow.

## Troubleshooting
- If you get authentication errors, verify your access token
- If API calls fail, check your application permissions
- Rate limiting may occur if making too many requests