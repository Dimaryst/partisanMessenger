import socket

package = "Test"
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

sock.connect(("200:5011:1b47:3a14:6322:c4c7:c24d:eff4", 41030))
sock.send(str(package).encode('utf-8'))

data = sock.recv(4096)
sock.close()
print(data.decode('utf-8'))