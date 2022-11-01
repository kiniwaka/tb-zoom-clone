import socket
import threading
#create a socket object
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind server to an ip with a port
serv.bind(('127.0.0.1',55555))
serv.listen()
clients = []
nicknames = []

#broadcast 
def broadcast(message):
    for client in clients:
        client.send(message)

#multicast should be used for private messages to individuals or groups

#handler
def handle(client):
    while True:
        try:
            #broadcasting messages
            #client is addressing all clients
            message = client.recv(1024)
            broadcast(message)
        except:
            #removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode())
            nicknames.remove(nickname)
            break

#receive function
def receive():
    while True:
        client, address = serv.accept()
        print("connected with {}".format(str(address)))
        
        #Request and STore nickname
        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        #Print and broadcast nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode())
        client.send('Connected to server!'.encode())
        
        #start handling thread for client
        thread = threading.Thread(target=handle, args = (client,))
        thread.start()

receive()
