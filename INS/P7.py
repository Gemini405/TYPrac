import ssl
import socket

context = ssl.create_default_context()
socket1 = socket.socket(socket.AF_INET)

wrapper = context.wrap_socket(socket1, server_hostname="example.com")
wrapper.connect(("example.com", 443))
wrapper.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

response = wrapper.recv(1024)
print(response.decode())

wrapper.close()
