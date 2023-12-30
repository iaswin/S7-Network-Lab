import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('127.1.1.0',8800)
while True:
	message1=input("enter the message to send")
	client.sendto(message1.encode(),server_address)


	data,address=client.recvfrom(1024)

	print(data.decode())

	if data.decode()=="hello client":
		break
