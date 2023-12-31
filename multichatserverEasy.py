import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.1.0.1',8800))

server.listen()


clients=[]



def broadcast(message):
	message1=message.encode()
	for client in clients:
		client.send(message1)



def handle(client,name):
	while True:
		message=client.recv(1024).decode()
		broadcast(f"{name}:{message}")




def recieve():
	while True:
		client,address=server.accept()
		print(f"connected with addresss {address}")
		name = f"user{len(clients) + 1}"
		clients.append(client)
		
		
		broadcast(f"{address} joined the chat")

		
		thread=threading.Thread(target=handle,args=(client,name))
		thread.start()
		

recieve()
	


