#!/usr/bin/env python3

#Using request and sys for multiple URL check
import sys
import requests

#urls = ["https://www.google.com", "https://github.com"]

def usage():
    print(f"Usage: python3 script.py <url>", file=sys.stderr)
    sys.exit(1)

def check_code(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        return response.status_code
    
    except requests.RequestException as e:
        print(f"URL: {url} failed to check Error: {e}")
    
def main():
    if len(sys.argv) < 2:
        usage()
    urls = sys.argv[1:]
    for url in urls:
        status_code = check_code(url)
        if status_code == 200:
            print(f"{url} ok")
        else:
            print(f"not ok")

if __name__ == "__main__":
    main()
