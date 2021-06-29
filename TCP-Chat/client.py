import threading
import socket

nickname=input('Choose your nickname')

host='localhost'
port=55401

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def recieve():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='Nick':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error has occured!!")
            client.close()
            break
def write():
    while True:
        message=f'{nickname}: {input(" ")}'
        client.send(message.encode('ascii'))
recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()