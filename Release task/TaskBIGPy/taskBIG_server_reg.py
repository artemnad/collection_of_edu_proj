import hashlib
import socket
import sys
import traceback
import re
from threading import Thread


if len(sys.argv) != 3:
    print('use -> taskBIG_server_chat.py 127.0.0.1 5555')
    exit()


def main():
    start_server()


def start_server():
    host = str(sys.argv[1])  # "127.0.0.1"
    port = int(sys.argv[2])  # 5555
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")
    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()
    soc.listen(33)
    print("Socket now listening")
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()
    soc.close()


def client_thread(connection, ip, port, max_buffer_size=4096):
    login = str(register_login(connection, ip, port, max_buffer_size))
    password = str(register_password(connection, ip, port, max_buffer_size))
    work_file = open('data.txt', 'a')
    work_file.write('\n' + login + ' ' + password)
    work_file.close()
    create_file = open('/users/' + login + '/.txt', 'a')
    create_file.close()
    connection.sendall('[Sign up is done]'.encode("utf8"))
    connection.close()
    print("Connection " + ip + ":" + port + " closed")


def register_login(connection, ip, port, max_buffer_size):
    connection.sendall('[Sign up]\nEnter your login (no more than 50 characters and no spaces):'.encode("utf8"))
    login = ''
    client_input = receive_input(connection, ip, port, max_buffer_size)
    work_file = open('data.txt', 'r')
    if not re.findall(client_input, work_file.read()):
        login = client_input
    else:
        print("Client has entered login that already exists")
        connection.sendall("This login already exists".encode("utf8"))
        connection.close()
        print("Connection " + ip + ":" + port + " closed")
    work_file.close()
    return login


def register_password(connection, ip, port, max_buffer_size):
    connection.sendall('Enter your password (no more than 50 characters and no spaces):'.encode("utf8"))
    client_input = receive_input(connection, ip, port, max_buffer_size)
    md5_hash = hashlib.md5(client_input.encode())
    password = md5_hash.hexdigest()
    return password


def receive_input(connection, ip, port, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    if sys.getsizeof(client_input) > 50 and re.findall(r'[ ]', client_input.decode("utf8").rstrip()):
        print("Client has entered more than 50 char or there is ' '")
        connection.sendall("You entered more than 50 char or there is ' '".encode("utf8"))
        connection.close()
        print("Connection " + ip + ":" + port + " closed")
    result = client_input.decode("utf8").rstrip()
    return result


if __name__ == "__main__":
    main()
