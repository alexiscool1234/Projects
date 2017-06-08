import socket
import threading


# set initial variables
host = socket.gethostname()
port = 6969


def main():
	# build the connection and start listening
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind((host, port))
	serverSocket.listen(5)
	print "Host %s listening on port %s" % (host, port)
	# loop infinitely and receive connections
	# start new thread for each new connection
	while True:
		conn, addr = serverSocket.accept()
		newThread = threading.Thread(target=file_transfer, args=(conn, addr, fileHeader, file))
		newThread.start()

	
def file_transfer(conn, addr, fileHeader, file):
	fileHeader = ""
	file = ""
	print "Threads: ", threading.active_count()
	print "Connection received from client", addr
	print "Transmission started"
	# loop to receive header characters until "@" is encountered
	fileHeaderBytes = conn.recv(1)
	if fileHeaderBytes == "\\":
		print "Client error, terminating connection."
		conn.close()
	else:
		while fileHeaderBytes != "/":
			fileHeader += fileHeaderBytes
			fileHeaderBytes = conn.recv(1)	
		# break up the header into filename, extension and filesize	
		fileName = fileHeader.split(".")[0]
		fileType = fileHeader.split(".")[1]
		fileSize = fileHeader.split(".")[2]
		# begin receiving the file, until no more data is sent
		receivedFile = conn.recv(1024)
		while receivedFile:
			file += receivedFile
			receivedFile = conn.recv(1024)
		# write the received data into the filename specified
		with open((fileName+"."+fileType), "wb") as newFile:
			newFile.write(file)		
		# confirm transfer is complete and close the connection	
		print "File transfer complete"
		conn.close()
		print "Host %s listening on port %s" % (host, port)

	
main()