#!/usr/bin/env python3
# Mulitple URL Checker with argparse

import sys
import requests
import argparse

def usage():
    print(f"Usage: python3 script.py <urls>", file=sys.stderr)
    sys.exit(1)

def check_code(url):
    try:
        response = requests.get(url, timeout=10, verify=True, allow_redirects=True)
        return response.status_code
    
    except requests.RequestException as e:
        print(f"Failed to check")
        return None

def main():
    if len(sys.argv) < 2:
        usage()

    parser = argparse.ArgumentParser(description=" This script will check multiple url and with argparse module") # create object
    parser.add_argument('urls', nargs='+', help="Provide valid URL")                                              # Add argument
    args = parser.parse_args()                                                                                    # pass the argument
    for url in args.urls:
        status_code = check_code(url)
        if status_code == 200:
            print(f"URL: {url} Status: {status_code}")
        else:
            print(f"URL {url} Status: failed")
            sys.exit(1)


if __name__ == "__main__":
    main()
