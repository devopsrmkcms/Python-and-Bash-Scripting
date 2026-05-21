Perfect 👍 — here are **20 real-world DevOps scripts using ONLY `socket`**  
👉 Small, practical, and easy to remember (your style 🔥)

***

# ✅ ✅ 1. Port Checker (Basic)

```python
import socket

s = socket.socket()
print("OPEN" if s.connect_ex(("google.com", 80)) == 0 else "CLOSED")
s.close()
```

***

# ✅ 2. Multi-Port Checker

```python
import socket

ports = [22, 80, 443]

for p in ports:
    s = socket.socket()
    print(p, "OPEN" if s.connect_ex(("google.com", p)) == 0 else "CLOSED")
    s.close()
```

***

# ✅ 3. TCP Connectivity Checker

```python
import socket

host = "github.com"

s = socket.socket()
print("Connected" if s.connect_ex((host, 443)) == 0 else "Failed")
s.close()
```

***

# ✅ 4. DNS Lookup

```python
import socket

print(socket.gethostbyname("google.com"))
```

***

# ✅ 5. Reverse DNS

```python
import socket

print(socket.gethostbyaddr("8.8.8.8"))
```

***

# ✅ 6. Simple TCP Client

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
print(s.recv(1024))

s.close()
```

***

# ✅ 7. Banner Grabbing

```python
import socket

s = socket.socket()
s.connect(("example.com", 80))

print(s.recv(1024))
s.close()
```

***

# ✅ 8. Timeout Handling

```python
import socket

s = socket.socket()
s.settimeout(2)

try:
    s.connect(("google.com", 81))
except:
    print("Timeout or closed port")
```

***

# ✅ 9. Local Host Info

```python
import socket

print(socket.gethostname())
```

***

# ✅ 10. Get Local IP

```python
import socket

print(socket.gethostbyname(socket.gethostname()))
```

***

# ✅ 11. Remote IP + Port Info

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

print("Remote:", s.getpeername())
s.close()
```

***

# ✅ 12. Client Socket Info

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

print("Local:", s.getsockname())
s.close()
```

***

# ✅ 13. Simple TCP Server

```python
import socket

s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(1)

conn, addr = s.accept()
print("Connected:", addr)
conn.close()
```

***

# ✅ 14. Echo Server

```python
import socket

s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(1)

conn, addr = s.accept()

msg = conn.recv(1024)
conn.send(msg)

conn.close()
```

***

# ✅ 15. UDP Sender

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello", ("127.0.0.1", 9999))
```

***

# ✅ 16. UDP Receiver

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))

data, addr = s.recvfrom(1024)
print(data)
```

***

# ✅ 17. Check Multiple Hosts

```python
import socket

hosts = ["google.com", "github.com"]

for h in hosts:
    try:
        print(h, socket.gethostbyname(h))
    except:
        print(h, "Failed")
```

***

# ✅ 18. Port Scanner (Mini)

```python
import socket

host = "google.com"

for p in range(79, 83):
    s = socket.socket()
    print(p, "OPEN" if s.connect_ex((host, p)) == 0 else "CLOSED")
    s.close()
```

***

# ✅ 19. HTTPS Port Check

```python
import socket

s = socket.socket()
print("HTTPS OK" if s.connect_ex(("google.com", 443)) == 0 else "FAIL")
s.close()
```

***

# ✅ 20. Full Simple Monitoring Script (🔥 BEST)

```python
import socket, sys

host = "google.com"

# DNS
try:
    ip = socket.gethostbyname(host)
    print("DNS:", ip)
except:
    print("DNS FAIL")
    sys.exit(1)

# PORT
s = socket.socket()
if s.connect_ex((host, 443)) != 0:
    print("PORT FAIL")
    sys.exit(2)

print("ALL OK ✅")
s.close()
```

***

# 🧠 Final Shortcut (IMPORTANT)

## ✅ 80% use-case pattern:

```python
s = socket.socket()
s.settimeout(3)
s.connect_ex((host, port))
s.close()
```

***

# 🚀 What You Can Do Now

With only `socket`, you can build:

✅ Port scanner  
✅ Network troubleshooting tool  
✅ Load balancer checks  
✅ DNS monitor  
✅ Connectivity validator

***

# 🔥 Next Level (Highly recommended)

If you want, I can give you:

✅ **Mini DevOps Monitoring Tool (single script)**  
✅ Combine socket + requests + alerts  
✅ Real interview questions + answers

Just say 👍
