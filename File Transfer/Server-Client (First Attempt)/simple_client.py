import socket

server = "127.0.0.1"
port = 6969
message_length = 0
sent = 0
data_to_send = ""

# prompt for file

target_file = raw_input("Please enter the filename you would like to send: ")
data_to_send += target_file + "1234x1234"
data_to_send += str(open(target_file).read())

# build the connection

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.connect((server, port))

# send the data

message_length = len(data_to_send)
transmission_complete = "6868"
newsocket.send(transmission_complete)

while sent != message_length:
	sent += newsocket.send(data_to_send)
	
transmission_complete = "6969"
newsocket.send(transmission_complete)
print "Transfer complete"
print newsocket.recv(1024)

# shut down the connection

newsocket.shutdown(1)
newsocket.close()