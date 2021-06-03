# простейшее сервер-приложение
import socket

# sock = socket.socket()
# sock.bind(('', 7777))
# sock.listen(1)
# conn, addr = sock.accept()

# print('Connected:', addr)

# data = conn.recv(1024)
# conn.send(data.upper())

# conn.close()

sock = socket.socket()
sock.bind(('', 8888))
sock.listen(1)
conn, addr = sock.accept()

print('Connected:', addr)
conn.send("ТЫ ДОЛЖЕН РЕШАТЬ ПРИМЕРЫ!!!!\n".encode())

while True:
    conn.send("2 + 2 = \n".encode())
    data = conn.recv(1024)
    if data.decode("utf-8") == "4\n":
        conn.send("correct\n".encode())
    else:
        conn.send("wrong\n".encode())