#!/usr/bin/env python3

# SINGLE URL CHECKER SCRIPT
import requests

URL = "https://www.google.com"  # Added https://

def check_url():
    response = requests.get(URL, timeout=10, allow_redirects=True)
    return response.status_code

def main():
    status_code = check_url()  # Added ()
    if status_code == 200:
        print(f"{URL} is working")  # Fixed f-string
    else:
        print(f"{URL} is not working (status: {status_code})")  # Improved output

if __name__ == "__main__":
    main()
