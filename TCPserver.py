import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port)) #1

server.listen(5) #2

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#client handling threading
def handle_client(client_socket): #3

	#print out what client sends 
	request = client_socket.recv(1024)

	print"[*] Received: %s" % request

	#send back a packet
	client_socket.send("ACK!")

	client_socket.close()

while True:

	client, addr = server.accept() #4

	print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

	#spin up our client thread to handle incoming data 
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start() #5
