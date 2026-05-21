Perfect 🔥 — this is **real DevOps-level practice**.  
Here are **20 combined scripts using `requests + socket + subprocess`** ✅

👉 Each script = **small, practical, interview-ready**

***

# ✅ ✅ 1. Website + Port Check

```python
import requests, socket

url = "https://google.com"
host = "google.com"

print(requests.get(url).status_code)

s = socket.socket()
print("Port 443:", "OPEN" if s.connect_ex((host, 443)) == 0 else "CLOSED")
s.close()
```

***

# ✅ 2. URL + Service Check

```python
import requests, subprocess

print(requests.get("https://google.com").status_code)

status = subprocess.run(["systemctl", "is-active", "sshd"], capture_output=True, text=True)
print(status.stdout.strip())
```

***

# ✅ 3. API + DNS Resolution

```python
import requests, socket

print(requests.get("https://api.github.com").status_code)
print(socket.gethostbyname("github.com"))
```

***

# ✅ 4. HTTP + Ping Check

```python
import requests, subprocess

print(requests.get("https://google.com").status_code)

ping = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True)
print("PING OK" if ping.returncode == 0 else "PING FAIL")
```

***

# ✅ 5. Multi URL + Port Monitor

```python
import requests, socket

urls = ["google.com", "github.com"]

for u in urls:
    print(requests.get(f"https://{u}").status_code)
    s = socket.socket()
    print("Port 80:", s.connect_ex((u, 80)) == 0)
    s.close()
```

***

# ✅ 6. Container + API Check

```python
import requests, subprocess

print(requests.get("https://google.com").status_code)

docker = subprocess.run(["docker", "ps"], capture_output=True, text=True)
print("Docker Running" if docker.stdout else "No Containers")
```

***

# ✅ 7. Service + DNS + HTTP

```python
import subprocess, socket, requests

print(socket.gethostbyname("google.com"))

svc = subprocess.run(["systemctl", "is-active", "crond"], capture_output=True, text=True)
print(svc.stdout.strip())

print(requests.get("https://google.com").status_code)
```

***

# ✅ 8. API + Response Time + Port

```python
import requests, time, socket

start = time.time()
requests.get("https://google.com")
print("Time:", time.time() - start)

s = socket.socket()
print("Port 443:", s.connect_ex(("google.com", 443)) == 0)
s.close()
```

***

# ✅ 9. URL + Host Reachability

```python
import requests, subprocess

print(requests.get("https://google.com").status_code)

ping = subprocess.run(["ping", "-c", "1", "google.com"])
print(ping.returncode)
```

***

# ✅ 10. API JSON + DNS

```python
import requests, socket

data = requests.get("https://api.github.com").json()
print(data["current_user_url"])

print(socket.gethostbyname("github.com"))
```

***

# ✅ 11. HTTP + TCP Banner Grab

```python
import requests, socket

print(requests.get("https://google.com").status_code)

s = socket.socket()
s.connect(("google.com", 80))
print(s.recv(1024))
s.close()
```

***

# ✅ 12. Multiple Services + API

```python
import subprocess, requests

services = ["sshd", "crond"]

for s in services:
    res = subprocess.run(["systemctl", "is-active", s], capture_output=True, text=True)
    print(s, res.stdout.strip())

print(requests.get("https://google.com").status_code)
```

***

# ✅ 13. Docker + Port + HTTP

```python
import subprocess, socket, requests

print(subprocess.run(["docker", "ps"], capture_output=True).returncode)

s = socket.socket()
print(s.connect_ex(("localhost", 80)) == 0)

print(requests.get("https://google.com").status_code)
```

***

# ✅ 14. Endpoint + Timeout + DNS

```python
import requests, socket

try:
    requests.get("https://google.com", timeout=2)
    print("HTTP OK")
except:
    print("Timeout")

print(socket.gethostbyname("google.com"))
```

***

# ✅ 15. Health Check (All-in-one)

```python
import requests, socket, subprocess

print("HTTP:", requests.get("https://google.com").status_code)

print("DNS:", socket.gethostbyname("google.com"))

svc = subprocess.run(["systemctl", "is-active", "sshd"], capture_output=True, text=True)
print("Service:", svc.stdout.strip())
```

***

# ✅ 16. SSL Port Check + HTTP

```python
import socket, requests

s = socket.socket()
print("443:", s.connect_ex(("google.com", 443)) == 0)
s.close()

print(requests.get("https://google.com").status_code)
```

***

# ✅ 17. Curl Alternative Script

```python
import requests, subprocess

print(requests.get("https://google.com").headers)

curl = subprocess.run(["curl", "-I", "https://google.com"], capture_output=True, text=True)
print(curl.stdout)
```

***

# ✅ 18. Remote Host Check

```python
import socket, subprocess

print(socket.gethostbyname("google.com"))

ping = subprocess.run(["ping", "-c", "1", "google.com"])
print(ping.returncode)
```

***

# ✅ 19. API + System Load

```python
import requests, subprocess

print(requests.get("https://api.github.com").status_code)

load = subprocess.run(["uptime"], capture_output=True, text=True)
print(load.stdout)
```

***

# ✅ 20. Full DevOps Monitor Script (🔥 BEST)

```python
import requests, socket, subprocess, sys

host = "google.com"

# HTTP
try:
    r = requests.get(f"https://{host}", timeout=3)
    print("HTTP:", r.status_code)
except:
    print("HTTP FAIL")
    sys.exit(1)

# DNS
print("DNS:", socket.gethostbyname(host))

# PORT
s = socket.socket()
if s.connect_ex((host, 443)) != 0:
    print("PORT FAIL")
    sys.exit(2)
s.close()

# SERVICE
svc = subprocess.run(["systemctl", "is-active", "sshd"], capture_output=True, text=True)
print("SERVICE:", svc.stdout.strip())

print("ALL OK ✅")
```

***

# 🧠 Final Learning Outcome

With these scripts, you now understand:

✅ HTTP checks (`requests`)  
✅ Network checks (`socket`)  
✅ System/service checks (`subprocess`)  
✅ Real monitoring logic

***

# 🚀 If you want next level (HIGH VALUE)

👉 I can give you:

* ✅ **Nagios-compatible plugin scripts**
* ✅ **Prometheus exporter Python script**
* ✅ **Full monitoring tool (mini project)**

Just say 👍
