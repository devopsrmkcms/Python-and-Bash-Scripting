Great 👍 — this is exactly your style: **top functions + small programs (easy to remember)**

I’ll give you **most important `requests` functions** with **tiny usable scripts** ✅

***

# ✅ ✅ Top Functions in `requests` (with mini programs)

***

# 🔹 1. `requests.get()` → Fetch data

```python
import requests

r = requests.get("https://api.github.com")

print(r.status_code)
print(r.text[:100])
```

***

# 🔹 2. `requests.post()` → Send data

```python
import requests

data = {"name": "rizwan"}

r = requests.post("https://httpbin.org/post", json=data)

print(r.status_code)
print(r.json())
```

***

# 🔹 3. `requests.put()` → Update resource

```python
import requests

data = {"name": "updated"}

r = requests.put("https://httpbin.org/put", json=data)

print(r.status_code)
```

***

# 🔹 4. `requests.delete()` → Delete resource

```python
import requests

r = requests.delete("https://httpbin.org/delete")

print(r.status_code)
```

***

# 🔹 5. `requests.head()` → Headers only

```python
import requests

r = requests.head("https://google.com")

print(r.headers)
```

***

# 🔹 6. `params` → Query parameters

```python
import requests

params = {"q": "devops"}

r = requests.get("https://httpbin.org/get", params=params)

print(r.url)
```

***

# 🔹 7. `headers` → Custom headers

```python
import requests

headers = {"User-Agent": "My-App"}

r = requests.get("https://httpbin.org/get", headers=headers)

print(r.request.headers)
```

***

# 🔹 8. `timeout` → Avoid hanging

```python
import requests

try:
    r = requests.get("https://google.com", timeout=3)
    print("Success")
except requests.Timeout:
    print("Timeout")
```

***

# 🔹 9. `auth` → Basic authentication

```python
import requests

r = requests.get("https://httpbin.org/basic-auth/user/pass",
                 auth=("user", "pass"))

print(r.status_code)
```

***

# 🔹 10. `json()` → Parse API response

```python
import requests

r = requests.get("https://api.github.com")

data = r.json()

print(data["current_user_url"])
```

***

# 🔹 11. `status_code` → Check response

```python
import requests

r = requests.get("https://google.com")

if r.status_code == 200:
    print("OK")
```

***

# 🔹 12. `raise_for_status()` → Error handling

```python
import requests

try:
    r = requests.get("https://httpbin.org/status/404")
    r.raise_for_status()
except requests.HTTPError:
    print("Error occurred")
```

***

# 🔹 13. `cookies` → Handle cookies

```python
import requests

r = requests.get("https://httpbin.org/cookies/set?name=value")

print(r.cookies)
```

***

# 🔹 14. `Session()` → Persistent connection

```python
import requests

s = requests.Session()

s.get("https://httpbin.org/cookies/set/name/value")
r = s.get("https://httpbin.org/cookies")

print(r.text)
```

***

# 🔹 15. `stream` → Download file

```python
import requests

r = requests.get("https://httpbin.org/image/png", stream=True)

with open("img.png", "wb") as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)
```

***

# ✅ ✅ Most Important for DevOps (Remember Only These 🔥)

👉 If short on time, focus:

* `get()`
* `post()`
* `status_code`
* `json()`
* `timeout`
* `headers`
* `auth`

***

# 🧠 Easy Pattern (VERY IMPORTANT)

```python
r = requests.get(url, timeout=5)
print(r.status_code)
print(r.text / r.json())
```
