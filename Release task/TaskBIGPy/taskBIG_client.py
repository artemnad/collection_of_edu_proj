import socket
import sys
from threading import Thread

if len(sys.argv) != 3:
    print('use -> taskBIG_client.py 127.0.0.1 6666 (for chat) or 5555 (for reg)')
    exit()


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()
    print("Enter '/quit' to exit")
    try:
        Thread(target=listen_for_messages, args=(soc,)).start()
        Thread(target=send_msg, args=(soc,)).start()
    except:
        print('Thread error')
        soc.close()


def listen_for_messages(soc):
    while True:
        message = soc.recv(4096).decode("utf8")
        print('\n' + message)


def send_msg(soc):
    while True:
        to_send = input('')
        if to_send.lower() == 'q':
            break
        soc.send(to_send.encode("utf8"))


if __name__ == "__main__":
    main()
