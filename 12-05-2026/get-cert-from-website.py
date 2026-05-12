import ssl
import socket

hostname = "google.com"
port = 443

cert = ssl.get_server_certificate((hostname, port))
print(cert)
