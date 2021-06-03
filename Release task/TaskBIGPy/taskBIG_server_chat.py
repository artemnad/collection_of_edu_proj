import hashlib
import socket
import sys
import traceback
import re
from threading import Thread


users = []
connection_list = []
if len(sys.argv) != 3:
    print('use -> taskBIG_server_chat.py 127.0.0.1 6666')
    exit()


def main():
    start_server()


def start_server():
    host = str(sys.argv[1])  # "127.0.0.1"
    port = int(sys.argv[2])  # 6666
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
    user = sign_in(connection, ip, port, max_buffer_size)
    connection_list.append(connection)
    users.append(user)
    while True:
        try:
            message = receive_input(connection, max_buffer_size)
            if message:
                print(user + ": " + message)
                message_to_send = user + ': ' + message
                broadcast(message_to_send, connection)
            else:
                remove(connection, user)
        except:
            continue


def broadcast(message_to_send, connection):
    for user in connection_list:
        if user != connection:
            try:
                user.send(message_to_send.encode("utf8"))
            except:
                user.close()
                remove(user, user)


def remove(connection, user):
    if connection in connection_list:
        connection_list.remove(connection)
    if user in users:
        users.remove(user)


def sign_in(connection, ip, port, max_buffer_size):
    connection.send('[Sign in]\nEnter your login:'.encode("utf8"))
    client_input = receive_input(connection, max_buffer_size)
    work_file = open('data.txt', 'r')
    log_and_pass = re.findall(client_input + r'[ ]\w+', work_file.read())
    work_file.close()
    log_and_pass = re.split(r' ', "".join(log_and_pass))
    if log_and_pass[0] and log_and_pass[0] not in users:
        connection.send('Enter your password:'.encode("utf8"))
        client_input = receive_input(connection, max_buffer_size)
        md5_hash = hashlib.md5(client_input.encode())
        password = md5_hash.hexdigest()
        if password == log_and_pass[1]:
            user = log_and_pass[0]
            connection.send('Welcome to chat'.encode("utf8"))
            return user
        else:
            print("Client has entered invalid password")
            connection.send("This password is not correct".encode("utf8"))
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
    else:
        print("The client entered a username that does not exist or is already in use")
        connection.send("login does not exist or is already in use".encode("utf8"))
        connection.close()
        print("Connection " + ip + ":" + port + " closed")


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    result = client_input.decode("utf8").rstrip()
    return result


if __name__ == "__main__":
    main()
