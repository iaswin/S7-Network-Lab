import socket
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.1.0.0',8800))
nickname=input("enter your nickname")

def recieve():
	while True:
		message=client.recv(1024).decode()
		if message=="NICKNAME":
			client.send(nickname.encode())
		else:
			print(message)
		

def send():
	while True:
		message=(f'{nickname}:{input(" ")}')
		client.send(message.encode())


recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()

send_thread=threading.Thread(target=send)
send_thread.start()


