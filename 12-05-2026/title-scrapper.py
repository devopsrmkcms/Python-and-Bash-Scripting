import requests
from bs4 import BeautifulSoup

url = input("Enter: ")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    print("Website Title:", title)

except requests.exceptions.RequestException as e:
    print("Error:", e)
