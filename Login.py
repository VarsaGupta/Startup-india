import requests

url = 'https://api.startupindia.gov.in/sih/api/noauth/sihLogin/auth'
headers = {
    'Content-Type': 'application/json',
    'Referer': 'https://www.startupindia.gov.in/',
    'Origin': 'https://www.startupindia.gov.in',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
    # Add other necessary headers if required
}

payload = {
    "username": "varsa.is21@bmsce.ac.in",
    "password": "Startup@@123",
    "grantType": "PASSWORD",
    "captchaResponse": "03AAYGu2SNcSf9lilvG9Tf16-D1RkfoylNeralz89HEQM_1u7h8JsrNy60y0cdutSlZNHk6go9Ean_FQ9zrOaqB3xrrIUWa0y5bo_ZHlCxORKYsDX4iczKxnj1iNES4ddBgfW9qIJhJQIIuyQuAkmUp91VrKwZk5tujzqbhf4Krb36HAnzGhabKJV32BpLrzBYCBXegr5rWsya3XOJwwAlNx2U2ZuhKFkX_S8dcra3mR_iOTd436pznETnnIB8HxN2QcY48mLo9f6rcWPQdRy_OkKfRwDz4y80pMk18TiujkXBE6ACKiQxUFS44-ws8w5f161q_VwwFUGygN1KQ9IvGU5pECWdBuqjEw7HRBVF1_5AslU_-8EjfdMn8_WkUTFL2zRa5d8WW03FtGzRI5IzsNI8fHyJAgb1o0XWdv7YSLo0Gmv0Q8RoPS72qOg1_nU16ZmhO54UKQlXidReNNAGYum3pBzDLAc6gje0pNHPbQDeFAyvNCJI8UzzntYMGlNfb8tl7ApK7ok0acbJPRihIfPJx6UT-b8P5DDfiKEJmLYJ4WJIaD4UgBuuX1THS44Md4AiYKSsJ"
}

response = requests.post(url, headers=headers, json=payload)

# Extract the CAPTCHA response from the payload
captcha_response = payload['captchaResponse']

# Use the extracted CAPTCHA response in the subsequent request
captcha_url = 'https://www.google.com/recaptcha/api2/userverify?k=6Ld112UUAAAAAITPMregPN1avoXBSMtFeOfra0_r'
captcha_payload = {
    'v': 'iZWPJyR27lB0cR4hL_xOX0GC',
    'c': captcha_response,
    't': '18101',
    'ct': '18100',
    'bg': '!p6GgoaQKAAQeBfR0bQEHDwBMjZnyEuNqUjRFVNjSSE14NwVKW0R13NwdSNqZnrVmL8xVDRxbfLSKnfmzwaxdr_RAhSqLyta_Xm0S1xr-wgAqU5OPMepPBSVVdI48YpwCs0zd6JTMLlIqsHdLcSzNAbiTohf95NMTN84hD24-Z2jCSa3vw0_LNv35j9AIakN9M7RD6trYw1aDMmGPmZDMsaPdUwRH7v7vFvfW-5UrcboNgBaZr1bRP5zApioieYQVjvr8yIMh3VITNwR6V7483N_YvSqfkmzAWk3mKhUYUdlsuSQ8q_Mekxx9cV6qRJ5M7W8zLvJN2bXnwdKiTjvQdr5EHmKZ1jMsIctEc1ysTssjVgDfVt991Wc3fsPkXODYp44vxeZyURclwtihpRtuoudyNmyPS_zdkJVSnED-tkRWp4HrfDWWT_UPGnvU7jG_eNCp3hARqeCO-1YvIL86N5YsY0wDNaABo2elhfy5TGPAPjZjWyWZ6i1g9tdxUxKAyk-hpChzk1TiTTg2pjQwZyPl3h0V2YJC2sa2DgDaKyFmPnbwWZfpsxjuUCg7wwHSfgpoafzZzgqSLOT41gXhvh4myxL25o54CUfd-iX-B_eF7B0RRvp3GjpPI0fP798SxXH0bZ5YVQAAoIy_lsL0Yoz8cc2xRhnQseq2xHYctSpEu920vZ1GYIQzchxmN3jPtgYEedy5fND5N5thLYTVGOrCVGRpKjV0rY63MMkWwYRglhi39M2JN_308HtGS9YF3gZ4tDxt5BLUSWKIIsNLN4v0SBp3P4RKDtgZ_YUsZUt_QnGEpxyCiyxfY48jEtGhkX_jZczXAIS6D5JwjM7Nqp528xA55eIXPASLJFInM-sF7kCgIvs10hriYheF7_dvJGn20Lcha4UVTZYnF1YahwKEjg1nODN7zKQ_Tb3zPv5WnlTATQzS_LZ8gV8JCD3GoehcSdmzbiltt5pNkCWNu88ySGTQBiatuyoC4Yq-nE2PCT58kgdmovIfFxGHOZcU5pSthdzSpHQifTBFUwzluJEr3XY',
    'response': captcha_response
}

captcha_response = requests.post(captcha_url, headers=headers, data=captcha_payload)

# Print the response status code and content
print('Response Status Code:', captcha_response.status_code)
print('Response Content:', captcha_response.text)
