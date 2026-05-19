Great 👍 — here are **most important `socket` module functions** with **very small, easy-to-remember examples** (DevOps focused).

***

# ✅ ✅ Top `socket` Functions + Mini Examples

***

# 🔹 1. `socket.socket()` → Create socket

```python
import socket

s = socket.socket()
print("Socket created")
```

***

# 🔹 2. `connect()` → Connect to remote host

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

print("Connected")
s.close()
```

***

# 🔹 3. `connect_ex()` → Safe connect (no crash)

```python
import socket

s = socket.socket()
result = s.connect_ex(("google.com", 80))

print("OPEN" if result == 0 else "CLOSED")
s.close()
```

***

# 🔹 4. `bind()` → Bind to IP + port (server)

```python
import socket

s = socket.socket()
s.bind(("0.0.0.0", 9999))

print("Bound to port")
```

***

# 🔹 5. `listen()` → Start listening (server mode)

```python
import socket

s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(5)

print("Listening...")
```

***

# 🔹 6. `accept()` → Accept client connection

```python
import socket

s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(1)

conn, addr = s.accept()
print("Connected from", addr)
```

***

# 🔹 7. `send()` → Send data

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
s.close()
```

***

# 🔹 8. `recv()` → Receive data

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
print(s.recv(1024))

s.close()
```

***

# 🔹 9. `close()` → Close connection

```python
import socket

s = socket.socket()
s.close()
print("Closed")
```

***

# 🔹 10. `settimeout()` → Timeout handling

```python
import socket

s = socket.socket()
s.settimeout(3)

try:
    s.connect(("google.com", 81))
except:
    print("Timeout or unreachable")
```

***

# 🔹 11. `gethostbyname()` → DNS lookup

```python
import socket

ip = socket.gethostbyname("google.com")
print(ip)
```

***

# 🔹 12. `gethostname()` → Local hostname

```python
import socket

print(socket.gethostname())
```

***

# 🔹 13. `gethostbyaddr()` → Reverse DNS

```python
import socket

print(socket.gethostbyaddr("8.8.8.8"))
```

***

# 🔹 14. `getsockname()` → Local socket info

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

print(s.getsockname())
s.close()
```

***

# 🔹 15. `getpeername()` → Remote socket info

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

print(s.getpeername())
s.close()
```

***

# 🔹 16. `setsockopt()` → Set socket options

```python
import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

***

# 🔹 17. `shutdown()` → Stop connection

```python
import socket

s = socket.socket()
s.connect(("google.com", 80))

s.shutdown(socket.SHUT_RDWR)
s.close()
```

***

# 🔹 18. `recvfrom()` → Receive (UDP)

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))

data, addr = s.recvfrom(1024)
print(data, addr)
```

***

# 🔹 19. `sendto()` → Send (UDP)

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b"Hello", ("127.0.0.1", 9999))
```

***

# 🔹 20. `setblocking()` → Blocking mode

```python
import socket

s = socket.socket()
s.setblocking(False)

print("Non-blocking mode")
```

***

# 🧠 MUST REMEMBER (Your Shortcut 🔥)

## ✅ Client pattern

```python
s = socket.socket()
s.connect((host, port))
s.send()
s.recv()
s.close()
```

***

## ✅ Server pattern

```python
s = socket.socket()
s.bind(("0.0.0.0", port))
s.listen()
conn, addr = s.accept()
conn.recv()
conn.send()
```

***

# 🚀 DevOps Use Cases

✔ Port checker  
✔ Network troubleshooting  
✔ Load balancer testing  
✔ Service connectivity validation  
✔ Custom monitoring tools

***

# ✅ If you want next step

I can give:

👉 20 real DevOps scripts using `socket` only  
👉 Port scanner full script  
👉 TCP/UDP tool (mini project)

Just say 👍
