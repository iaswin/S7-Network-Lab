import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8899))

while True:
	message=input("enter the message")
	client.send(message.encode())
