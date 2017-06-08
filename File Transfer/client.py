import socket
import os


def main():
	while True:
		host = raw_input("Please enter a server to connect to: ")
		print "\nAttempting to connect to server: %s on port %s" % (host, port)
		# build connection to server
		try:
			clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			clientSocket.connect((host, port))
		except:
			print "Failed to connect, please try again."
			main()	
		file_transfer(clientSocket)


def file_transfer(clientSocket):
	totalSent = 0
	# prompt use for file to be sent
	fileName = raw_input("Please enter the file you would like to send: ")
	# try and open file
	try:
		openedFile = open(fileName, "rb")
	except:
		print "Error opening file, exiting."
		clientSocket.send("\\")
		clientSocket.close()
		exit()
	# get file size and build the header to be sent to server
	fileSize = int(os.path.getsize(fileName))
	fileHeader = fileName + "." + str(fileSize) + "/"
	# send the header
	clientSocket.send(fileHeader)
	# read the file specified in a 1024 chunk
	readFile = openedFile.read(1024)
	# loop until data sent = filesize
	while totalSent < fileSize:	
		clientSocket.send(readFile)
		totalSent += len(readFile)
		readFile = openedFile.read(1024)
	# print confirmation of transfer and close connection
	print "Transmission complete"
	print "Closing connection"
	clientSocket.close()
	
	
main()