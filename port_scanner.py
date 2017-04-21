import socket
import sys


def port_scan(ipaddress, start, end):

	open_ports = {}
	closed_ports = {}

	""" This function carries out the port scan, and returns two dictionaries containing Open and Closed ports respectively """
	
	print "\nStarting to scan host '%s' for range '%s-%s'\n" % (ipaddress, start, end)
	
	for port in range(start,(end+1)): # scans the specified range, adding 1 to be inclusive of the end port
	
		newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# open a new socket using IPv4, using TCP
		status = newsocket.connect_ex((ipaddress, port))
		
		if status == 0: 	# port open
			newsocket.close()
			open_ports[port] = "Open"
		else: 				# port closed
			newsocket.close()
			closed_ports[port] = "Closed"
		
		sys.stdout.write("\rScanning port %s / %s" % (port, end))	# write a status bar for the scan
		sys.stdout.flush()											# flush the line so it looks like a single updating digit
		
	print "\nScan completed!"
	return open_ports, closed_ports


def write_report(open_ports, closed_ports):

	""" This function takes the scan result dictionaries and outputs them in a formatted way to 'report.txt' """
	
	reportfile = open("report.txt", "w+")
	reportfile.write("*" * 60 + "\n")
	reportfile.write("Results:\n")
	reportfile.write("*" * 60 + "\n\n")
	reportfile.write("-------------\nOpen ports:\n-------------\n")
	
	if bool(open_ports) == True:
		for key,value in open_ports.items():
			reportfile.write("\n%s: %s" % (key,value))
	else:
		reportfile.write("\n0")

	reportfile.write("\n\n-------------\nClosed ports:\n-------------\n")
	if bool(closed_ports) == True:
		for key,value in closed_ports.items():
			reportfile.write("\n%s: %s" % (key,value))
	else:
		reportfile.write("\n0")
	
	reportfile.write("\n\n")
	reportfile.close()


def print_report():

	""" This function takes 'results.txt' and outputs it on screen """
	
	reportfile = open("report.txt", "r")
	print "\n"
	print reportfile.read()


def main():

	""" Main program, walks the user through a port scan """

	print "*" * 60
	print "Port Scanner (ultimate meme edition)"
	print "*" * 60

	ipaddress = str(raw_input("Please enter an IP address: "))
	start = int(raw_input("Please enter the start of the range to scan: "))
	end = int(raw_input("Please enter the end of the range to scan: "))
	a, b = port_scan(ipaddress, start, end)
	write_report(a, b)
	z = raw_input("Would you like to view the results? (yes/no): ")

	if z == "yes":
		print_report()
	else:
		pass
		
main()