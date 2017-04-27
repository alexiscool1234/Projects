import socket
import os

# set server details (might accept user input in future)

host = "al-car-05791"
port = 6969
totalSent = 0

print "Connecting to host", host

# build connection to server

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

# prompt use for file to be sent

fileName = raw_input("Please enter the file you would like to send: ")
openedFile = open(fileName, "rb")

# get file size and build the header to be sent to server

fileSize = int(os.path.getsize(fileName))
fileHeader = fileName + "." + str(fileSize) + "@"

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