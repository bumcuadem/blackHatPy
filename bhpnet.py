import sys
import socket
import getopt
import threading
import subprocess

#define some global vars
listen = False 
command = False 
upload = False 
execute = ""
target = ""
upload_destination = ""
port = 0

def usage(): #1
	print("""BHP Net Tool

		     Usage: bhpnet.py -t target_host -p port
		     -l --listen              - listen on [host]:[port] for
		                                incoming connections		     
		     -e --execute=file_to_run - execute the given file upon                          
		     							receiving a connection
		     -c --command             - initialize a command shell
     	     -u --upload=destination  - upon receiving connection upload a
     	     							file and write to [destination]


     	     Examples:
     	     bhpnet.py -t 192.168.0.1 -p 5555 -l -c 
     	     bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe
     	     bhpnet.py -t 192.168.0.1 -p 5555 -l -e\"cat /etc/passwd\"
		     echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135
		     sys.exit(0)
		     """)
def client_sender(buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		#connect to our target host
		client.connect((target,port))
def main():
	global listen
	global port 
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()
	#2 read the commandline options
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
		["help", "listen", "execute", "target", "port", "command", "upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h", "--help"):
			usage()
		elif o in ("-l", "--listen"):
			listen = True
		elif o in ("-e", "--execute"):
			execute = a
		elif o in ("-c", "--commandshell"):
			command = True
		elif o in ("-u", "--upload"):
			upload_destination = a
		elif o in ("-p", "--port"):
			port = int(a)
		else:
			assert False,"Unhandled Option"
	#Listen or send data from stdin?
	if not listen and len(target) and port > 0:#3
		#read in from command line
		#this will block, so send CTRL-D if not sending input
		#to stdin
		buffer = sys.stdin.read()

		#send data off
		client_sender(buffer)
	#Listen and possibly upload,
	#execute commands, and drop shell back 
	#depending on options taken in above
	if listen:
		server_loop()#4
main()
