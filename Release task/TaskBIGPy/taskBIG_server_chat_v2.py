import hashlib
import socket
import sys
import traceback
import re
from threading import Thread


max_buffer_size = 4096
connection_list = {}
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


def client_thread(connection, ip, port):
    user = sign_in(connection, ip, port)
    connection_list[user] = connection
    connection.send(("1. list - выводит список всех пользователей, зашедших в данный чат;\n"
                     "2. whitelist - выводит список пользователей, общение с котроми возможно\n"
                     "(то есть всех пользователей, кроме входящих в 'чёрный список' данного\n"
                     "пользователя и добавивших данного пользователя в свой 'чёрный список');\n"
                     "3. blacklist - выводит чёрный список данного пользователя;\n"
                     "4. block <username> - добавляет пользователя в 'чёрный список';\n"
                     "5. unblock <username> - убирает пользователя из 'чёрного списка';\n"
                     "6. chat <username> - начать чат с пользователем username.").encode("utf8"))
    while True:
        try:
            message = receive_input(connection)
            select_cmd(connection, user, message)
        except:
            continue


def remove(connection, user):
    if connection in connection_list[user]:
        del connection_list[user]


def sign_in(connection, ip, port):
    connection.send('[Sign in]\nEnter your login:'.encode("utf8"))
    client_input = receive_input(connection)
    work_file = open('data.txt', 'r')
    log_and_pass = re.findall(client_input + r'[ ]\w+', work_file.read())
    work_file.close()
    log_and_pass = re.split(r' ', "".join(log_and_pass))
    if log_and_pass[0] and log_and_pass[0] not in connection_list.keys():
        connection.send('Enter your password:'.encode("utf8"))
        client_input = receive_input(connection)
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


def select_cmd(connection, user, cmd):
    cmd = re.split(r' ', cmd)
    select_dict = {'list': show_list(connection),
                   'whitelist': show_whitelist(connection, user),
                   'blacklist': show_blacklist(connection, user),
                   'block': block(connection, user, cmd[1]),
                   'unblock': unblock(connection, user, cmd[1]),
                   'chat': begin_chat(connection, user, cmd[1])}
    correct_cmd = select_dict.get(cmd[0])
    return correct_cmd


def show_list(connection):
    for other_user in connection_list.keys():
        connection.send(other_user.encode("utf8"))


def show_whitelist(connection, user):
    blacklist_file = open('/users/' + user + '/.txt', 'r')
    my_blacklist = blacklist_file.readlines()
    blacklist_file.close()
    other_blacklist = []
    for other_user in connection_list.keys():
        buff_blacklist_file = open('/users/' + other_user + '/.txt', 'r')
        buff_blacklist = buff_blacklist_file.readlines()
        buff_blacklist_file.close()
        if user == buff_blacklist:
            other_blacklist.append(other_user)
    for other_user in connection_list.keys():
        if other_user != my_blacklist and other_user != other_blacklist:
            connection.send(other_user.encode("utf8"))


def show_blacklist(connection, user):
    blacklist_file = open('/users/' + user + '/.txt', 'r')
    blacklist = blacklist_file.readlines()
    blacklist_file.close()
    for other_user in blacklist:
        connection.send(other_user.encode("utf8"))


def block(connection, user, block_user):
    blacklist_file = open('/users/' + user + '/.txt', 'a')
    blacklist_file.write('\n' + block_user)
    blacklist_file.close()
    msg = 'User ' + block_user + ' added to blacklist'
    connection.send(msg.encode("utf8"))


def unblock(connection, user, block_user):
    old_blacklist_file = open('/users/' + user + '/.txt', 'r')
    blacklist = old_blacklist_file.readlines()
    old_blacklist_file.close()
    new_blacklist_file = open('/users/' + user + '/.txt', 'w')
    for other_user in blacklist:
        if other_user != block_user:
            new_blacklist_file.write('\n' + other_user)
    new_blacklist_file.close()
    msg = 'User ' + block_user + ' removed from the blacklist'
    connection.send(msg.encode("utf8"))


def begin_chat(connection, user, interlocutor):
    msg = 'User ' + user + ' wants to start chat with you. Start chat?'
    connection_list[interlocutor].send(msg.encode("utf8"))
    interlocutor_input = receive_input(connection_list[interlocutor])
    if interlocutor_input == 'yes':
        msg = 'User ' + interlocutor + ' start a chat with you.'
        connection.send(msg.encode("utf8"))
        while True:
            message = receive_input(connection)
            if message:
                print(user + ": " + message)
                message_to_send = user + ': ' + message
                broadcast_one_on_one(message_to_send, connection, interlocutor)
            else:
                remove(connection, user)
    elif interlocutor_input == 'no':
        msg = 'User ' + interlocutor + '  does not want to start a chat with you.'
        connection.send(msg.encode("utf8"))


def broadcast_one_on_one(message_to_send, connection, interlocutor):
    connections_user = connection_list[interlocutor]
    try:
        connections_user.send(message_to_send.encode("utf8"))
    except:
        connections_user.close()
        remove(connection, interlocutor)


# not used for the second option
def broadcast(message_to_send, connection):
    for user_key, connections_user in connection_list.items():
        if connections_user != connection:
            try:
                connections_user.send(message_to_send.encode("utf8"))
            except:
                connections_user.close()
                remove(connection, user_key)


def receive_input(connection):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    result = client_input.decode("utf8").rstrip()
    return result


if __name__ == "__main__":
    main()
