import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.1.0.0',8800))

server.listen()


clients=[]
nicknames=[]


def broadcast(message):
	message1=message.encode()
	for client in clients:
		client.send(message1)



def handle(client):
	while True:
		message=client.recv(1024).decode()
		broadcast(message)




def recieve():
	while True:
		client,address=server.accept()
		print(f"connected with addresss {str(address)}")
		client.send("NICKNAME".encode())
		nickname=client.recv(1024).decode()
		nicknames.append(nickname)
		clients.append(client)
		print(f"nickname of client is {nickname}")
		broadcast(f"{nickname} joined the chat")
		
		thread=threading.Thread(target=handle,args=(client,))
		thread.start()
		

recieve()
	


