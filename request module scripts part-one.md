Perfect 👍 — here are **20 real-world `requests` scripts** (DevOps-focused, small, practical, easy to remember).

***

# ✅ ✅ 1. Website Health Check

```python
import requests

r = requests.get("https://google.com", timeout=5)
print("OK" if r.status_code == 200 else "DOWN")
```

***

# ✅ 2. API Status Checker

```python
import requests

r = requests.get("https://api.github.com")

print(r.status_code)
```

***

# ✅ 3. Response Time Monitor

```python
import requests, time

start = time.time()
requests.get("https://google.com")
print(f"Time: {time.time() - start:.2f}s")
```

***

# ✅ 4. JSON API Fetch

```python
import requests

data = requests.get("https://api.github.com").json()
print(data["current_user_url"])
```

***

# ✅ 5. POST API (send data)

```python
import requests

r = requests.post("https://httpbin.org/post", json={"user": "rizwan"})
print(r.json())
```

***

# ✅ 6. Auth API Call

```python
import requests

r = requests.get("https://httpbin.org/basic-auth/user/pass",
                 auth=("user", "pass"))
print(r.status_code)
```

***

# ✅ 7. Custom Headers

```python
import requests

headers = {"User-Agent": "DevOps-Agent"}
r = requests.get("https://httpbin.org/get", headers=headers)
print(r.request.headers)
```

***

# ✅ 8. Service Monitor (multiple URLs)

```python
import requests

urls = ["https://google.com", "https://github.com"]

for url in urls:
    try:
        r = requests.get(url, timeout=3)
        print(f"{url}: {r.status_code}")
    except:
        print(f"{url}: DOWN")
```

***

# ✅ 9. Download File

```python
import requests

r = requests.get("https://httpbin.org/image/png")

with open("img.png", "wb") as f:
    f.write(r.content)
```

***

# ✅ 10. Stream Large File

```python
import requests

r = requests.get("https://httpbin.org/image/png", stream=True)

for chunk in r.iter_content(1024):
    print("Chunk received")
```

***

# ✅ 11. Check Redirect

```python
import requests

r = requests.get("http://github.com", allow_redirects=True)

print(r.url)
```

***

# ✅ 12. Timeout Handling

```python
import requests

try:
    requests.get("https://google.com", timeout=1)
except requests.Timeout:
    print("Timeout")
```

***

# ✅ 13. Headers Info

```python
import requests

r = requests.get("https://google.com")
print(r.headers)
```

***

# ✅ 14. Cookies Handling

```python
import requests

r = requests.get("https://httpbin.org/cookies/set/name/value")
print(r.cookies)
```

***

# ✅ 15. Session Example (login-like)

```python
import requests

s = requests.Session()
s.get("https://httpbin.org/cookies/set/test/value")
print(s.get("https://httpbin.org/cookies").text)
```

***

# ✅ 16. Delete API Call

```python
import requests

r = requests.delete("https://httpbin.org/delete")
print(r.status_code)
```

***

# ✅ 17. PUT API Call

```python
import requests

r = requests.put("https://httpbin.org/put", json={"name": "new"})
print(r.status_code)
```

***

# ✅ 18. Check Content Type

```python
import requests

r = requests.get("https://api.github.com")
print(r.headers["Content-Type"])
```

***

# ✅ 19. Monitor JSON Field

```python
import requests

data = requests.get("https://api.github.com").json()

if "current_user_url" in data:
    print("Field Exists")
```

***

# ✅ 20. Simple Alert Script

```python
import requests

r = requests.get("https://google.com")

if r.status_code != 200:
    print("ALERT: Website Down")
```

***

# 🧠 Final Shortcut (Remember this)

👉 Most scripts = this pattern:

```python
import requests

r = requests.get(url, timeout=5)

print(r.status_code)
print(r.text or r.json())
```

***

# 🚀 What you just built

With these 20 scripts you can:

✅ Monitor APIs  
✅ Validate services  
✅ Automate CI/CD checks  
✅ Build health check tools  
✅ Integrate alerts

***

If you want next step 🔥  
I can give you:

👉 **20 combined DevOps scripts (requests + socket + subprocess)**  
👉 **Real monitoring tool script (like Nagios plugin)**
