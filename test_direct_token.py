import requests

# Direct token (from .env file)
token = "AQVt3FqbHT1JgOlznPW_ZHGUTRlwvLhXmfbucM0vDZ6w91_qFNaR6PEYiMlFDqyTJz8uNMGACWRdS_IshONt6Ip7xxqLRYvexDYrhLf3k82Uw1jlvmYVKRLKLLeP8hECxJivXc0FeFObDff8xiaTfjc2UWtsMpgJEJTy_fofEXFIs9ktVTn1MWdMbvRABlKK24G52HDIgt3QAILadyZLuZhNVkeNxilPgE8MmX9oKyHGD0EmjdsZWAgobz6b4AzdYXBU5NBvWJ1XVDYlbgM6h3evV9z14n9uw9pT-5Wk6iPP3TdhgMXvNWfPLUh2zGy7qexdrGpUmZjEQ_rEt3x7E0gk7iA-zQ"

print("Testing LinkedIn API with direct token...")
print("=" * 60)

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Test Profile
print("\n1. Testing Profile...")
response = requests.get('https://api.linkedin.com/v2/me', headers=headers)
print(f"   Status: {response.status_code}")
print(f"   Response: {response.text[:200]}")

if response.status_code == 200:
    print("   SUCCESS! Token is working!")
    data = response.json()
    print(f"   Name: {data.get('localizedFirstName', 'N/A')}")
elif response.status_code == 401:
    print("   ERROR: Token is invalid or revoked")
    print("   Try generating a NEW token from LinkedIn")
elif response.status_code == 403:
    print("   ERROR: Insufficient permissions")
    print("   Check app scopes in LinkedIn Developer Portal")
else:
    print(f"   Status: {response.status_code}")

print("\n" + "=" * 60)