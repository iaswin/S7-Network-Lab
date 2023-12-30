import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8899))
server.listen()

while True:
	client_socket,client_address=server.accept()
	print(f"connected to {client_address}")
	message=client_socket.recv(1024)
	print(message.decode())
	
