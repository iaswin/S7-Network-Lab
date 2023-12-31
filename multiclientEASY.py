import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.1.0.1', 8800))


def receive():
    while True:
        message = client.recv(1024).decode()
        print(message)


def send():
    while True:
        message = input("Enter your message: ")
        client.send(message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()



