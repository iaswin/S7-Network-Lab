import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.1.1.0',8800))

while True:
	username=input("enter the name")
	client.send(username.encode())
	message=input(f"{username}:")
	client.send(message.encode())
