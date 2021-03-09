import socket

# Creating socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host 192.168...
host = socket.gethostname()
print('Host name: ' + host)
port = 8081

# Including the socket
server.bind((host, port))

# Start TCP listener
server.listen(5)

while True:
    # Starting connection
    client, address = server.accept()
    print("Client: " + str(address))

    msg = 'Hello from server' + '\r\n'
    client.send(msg.encode('ascii'))
    client.close()
