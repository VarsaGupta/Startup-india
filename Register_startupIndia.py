import requests

url = 'https://api.startupindia.gov.in/sih/api/noauth/sihUser/register'
headers = {
    'Content-Type': 'application/json',
   'Origin': 'https://www.startupindia.gov.in',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
    # Add other necessary headers if required
}

payload = {
    'fullName': 'satvik',
    'email': 'satvikmishra2615@gmail.com',
    'mobile': '6204206589',
    'password': 'Satvik@153',
    'confirmPassword': 'Satvik@153'
}

response = requests.post(url, headers=headers, json=payload)

# Print the response status code and content
print('Response Status Code:', response.status_code)
print('Response Content:', response.text)
