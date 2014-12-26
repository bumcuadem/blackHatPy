import socket

target_host = os.getenv(IP, 0.0.0.0)
target_port = os.getenv(PORT, 8080)

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data
client.sendto("AAABBBCCC", (target_host, target_port))

#receive data
data, addr = client.recvfrom(4096)

print data