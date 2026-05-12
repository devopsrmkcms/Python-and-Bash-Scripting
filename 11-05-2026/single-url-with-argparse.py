#!/usr/bin/env python3

# Single URL Checker using requests and argparse

import requests
import sys
import argparse     # module imported

def usage():
    print(f"Usage: python3 script.py <url>", file=sys.stderr)
    sys.exit(1)

def check_https_code(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True, verify=True)
        return response.status_code
    
    except requests.RequestException as e:
        print(f"{url} failed with {e}")

def main():
    parser = argparse.ArgumentParser(description= "This script will check hhtps status code for url")  # create object
    parser.add_argument('url', help="provide url")                                                     # add argument
    args = parser.parse_args()                                                                         # Pass the argument
    if len(sys.argv) < 2:
        usage()

    status_code = check_https_code(args.url)
    if status_code == 200:
        print(f"URL: {args.url} Status: ok")
        sys.exit(0)
    else:
        print(f"URL {args.url} Status: Failed")
        sys.exit(1)

    
if __name__ == "__main__":
    main()
