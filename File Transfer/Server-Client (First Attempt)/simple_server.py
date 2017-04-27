import socket

host = ""
port = 6969

# set up the socket

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.bind((host, port))

# set it to listen for connections and loop

newsocket.listen(10)

while True:

	print "Listening for connection"
	connection, address = newsocket.accept()
	received_data = connection.recv(4)
	received_data = ""
	
	while "6969" not in received_data:
		received_data += connection.recv(4096)
		
	received_data = received_data[:-4]
		
	# save received data to a file
	
	name_of_file = received_data.split("1234x1234")[0]
	
	with open(name_of_file, "w") as newfile:
		newfile.write(received_data.split("1234x1234")[1])
		newfile.close()
	
	print "Transfer complete"
	connection.sendall("Safe fam")
	connection.close()
	received_data = ""

newsocket.close()