from dotenv import load_dotenv
import os
import requests

# Load token from .env
load_dotenv()

access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')

print("=" * 60)
print("LINKEDIN API TEST")
print("=" * 60)

if not access_token:
    print("ERROR: Token not found in .env file!")
    exit()

print(f"OK: Token loaded: {len(access_token)} characters")

# Test headers
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

print(f"\nTesting API endpoints...")
print("=" * 60)

# Test 1: Basic Profile
print("\n1. Testing Profile Endpoint...")
try:
    profile_url = "https://api.linkedin.com/v2/me"
    response = requests.get(profile_url, headers=headers)
    print(f"   Status: {response.status_code}")
    
    if response.status_code == 200:
        print("   SUCCESS: Profile accessible!")
        data = response.json()
        print(f"   Name: {data.get('localizedFirstName', 'N/A')}")
    elif response.status_code == 401:
        print("   ERROR: Invalid token")
        print(f"   Response: {response.text}")
    elif response.status_code == 403:
        print("   ERROR: Insufficient permissions")
        print(f"   Response: {response.text}")
    else:
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")
except Exception as e:
    print(f"   ERROR: {e}")

# Test 2: Messages (This is what watcher uses)
print("\n2. Testing Messages Endpoint...")
try:
    messages_url = "https://api.linkedin.com/v2/conversationMessages"
    params = {'q': 'participants', 'participant.urn': 'urn:li:person:(self)'}
    response = requests.get(messages_url, headers=headers, params=params)
    print(f"   Status: {response.status_code}")
    
    if response.status_code == 200:
        print("   SUCCESS: Messages accessible!")
        data = response.json()
        elements = data.get('elements', [])
        print(f"   Found {len(elements)} messages")
    elif response.status_code == 401:
        print("   ERROR: Invalid token")
        print(f"   Response: {response.text}")
    elif response.status_code == 403:
        print("   ERROR: Insufficient permissions for Messages API")
        print(f"   Response: {response.text}")
        print("\n   NOTE: LinkedIn Messaging API requires special approval!")
    else:
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")
except Exception as e:
    print(f"   ERROR: {e}")

# Test 3: Posts/Social (w_member_social scope)
print("\n3. Testing Posts/Social Endpoint...")
try:
    posts_url = "https://api.linkedin.com/v2/personActions"
    response = requests.get(posts_url, headers=headers)
    print(f"   Status: {response.status_code}")
    
    if response.status_code == 200:
        print("   SUCCESS: Posts accessible!")
    elif response.status_code == 403:
        print("   ERROR: Insufficient permissions for Posts")
        print(f"   Response: {response.text}")
    else:
        print(f"   Status: {response.status_code}")
except Exception as e:
    print(f"   ERROR: {e}")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
