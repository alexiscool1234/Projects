import socket

host = ""
port = 6969

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.bind((host, port))

newsocket.listen(10)

while True == True:
	print "Listening for connection"
	connection, address = newsocket.accept()
	received_data = connection.recv(1024)
	print received_data
	connection.sendall("Safe fam")
	connection.close()

newsocket.close()