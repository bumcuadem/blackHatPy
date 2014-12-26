import sys
import socket
import threading

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((local_host, local_port))
    except:
            print"[!!] Failed to listen on: %s:%d" % (local_host,
            local_port)
            print"[!!] Check for other listening sockets or correct permissions."
            sys.exit(0)
            print "[*] Listening on %s:%d" % (local_host, local_port)
            
            server.listen(5)
            
            while True:
                client_socket, addr = server.accept()
                
                #print out the local conn
                print "[==>] Received incoming connection from %s:%d" %
                (addr[0], addr[1])
                
                #start thread for remote host
                proxy_thread = threading.Thread(target=proxy_handler, 
                args= (client_socket,remote_host,remote_port,receive_first))
                
                proxy_thread.start()

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    
    #connect to remote
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remoteport))
    
    #recv data from remote
    if receive_first:
            
            remote_buffer = receive_from(remote_socket)
            hexdump(remote_buffer)
            
            #send to response handler
                
def main():
    #[1:] everything after script name up to 5 args
    if len(sys.argv[1:]) != 5:
        print """Usage: ./tcpProxy.py [localhost] [localport] [remotehost]
        [remote port] [receive_first]"""
        print "Example: ./tcpProxy.py 127.0.0.1 1337 10.12.132.1 1337 True"
        sys.exit(0)
        
    #set up local listening port
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    
    #remote target
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    
    #tell proxy to connect and recv
    #before sending to remote
    receive_first = sys.argv[5]
    
    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False
    
    #turn up listener
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)
    
main()
