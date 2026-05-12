#!/usr/bin/env python3

# Single URL Checker using request and sys module

import sys
import requests

#url = "https://www.google.com"

def usage():
    print(f"Usage: python3 script.py <url> ", file=sys.stderr)
    sys.exit(1)

def check_url(url):
    try:
        resposne = requests.get(url, timeout=10, allow_redirects=True)
        return resposne.status_code
    except requests.RequestException as e:
        print(f"{url} is not reachable")

def main():
    if len(sys.argv) < 2:
        usage()
    
    url = sys.argv[1]
    status_code = check_url(url)
    
    if status_code == 200:
        print(f"{url} is working")
        sys.exit(0)
    else:
        print(f"{url} is not working")
        sys.exit(1)
if __name__ == "__main__":
    main()
