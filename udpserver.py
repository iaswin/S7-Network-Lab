import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.1.1.0',8800))

while True:
	message,client_address=server.recvfrom(1024)
	print(message.decode())

	server.sendto("hello client message recieved ".encode(),client_address)
