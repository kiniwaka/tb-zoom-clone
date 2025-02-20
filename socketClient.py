import socket
import threading

nickname = input("Choose your nickname: ")

#Connecting to server
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

#listening to serving and sending nickname
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

#sending messages to server
def write():
    while True:
        try:
            message = '{}: {}'.format(nickname,input(''))
            client.send(message.encode())
        except:
            print("An error occured!")


#starting threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

