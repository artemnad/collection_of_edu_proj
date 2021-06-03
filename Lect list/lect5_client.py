# простейшее клиент-приложение
import socket

# sock = socket.socket()
# sock.connect(('localhost', 7777))

# msg = input("Enter your message: ")
# sock.send(msg.encode())
# data = sock.recv(1024)
# print("The reply is:", data.decode("utf-8"))

# sock.close()

# sock = socket.socket()
# sock.connect(('math.csu.ru', 80))
# sock.send("GET /\n".encode())
# data = sock.recv(160000)
# print(data.decode("utf-8"))

sock = socket.socket()
sock.connect(('localhost', 8888))
data = sock.recv(1024)
print(data.decode("utf-8"))

while True:
    data = sock.recv(1024)
    print(data.decode("utf-8"))
    sock.send("4\n".encode())
    data = sock.recv(1024)
    print(data.decode("utf-8"))
