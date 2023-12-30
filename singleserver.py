import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.1.1.0',8800))

server.listen()

while True:
	client_socket,client_address=server.accept()
	message1=client_socket.recv(1024)
	username=message1.decode()
	print(f"got connection from {username}")
	message2=client_socket.recv(1024)
	print(f'{username}:{message2.decode()}')
	
