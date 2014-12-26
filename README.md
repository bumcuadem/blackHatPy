TCP Client

1. Create socket object using AF_INET and SOCK_STREAM.
	- AF_INET = use standard IPv4 address or hostname.
	- SOCK_STREAM indicates that it will be a TCP client. 
2. Connect client to server.
3. Send some data to server.
4. Receive some data back.

UDP Client

1. Change socket type to SOCK_DGRAM.
2. Call sento() pass in the data and server.
3. UDP is connectionless so no need to use connect()
4. Receive some data back.

TCP Server

1.Pass in IP and Port
2.Limit backlog of connections to 5
3.Handle_client function performs the recv() and sends simple message back to client.
4.When client connects assign to variable, create new thread object that points
	to Handle_client function. Pass it the client socket object as argument.
5.Example output:
	[*] Listening on 0.0.0.0:9999
	[*] Accepted connection from: 127.0.0.1:62512
	[*] Received: ABCDEF

BHP Net Tool
1. Print out usage information
2.Read command line options 
3.Mimic NetCat to read from stdin
4.Set up listening socket to take in options

tcpProxy

