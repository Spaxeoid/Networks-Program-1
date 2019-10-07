# Email Server
# Timothy Leach
# Due 10/07/2019

from socket import *
import sys
import glob
import os
import os

def stat():
    count = 0
    size = 0
    for e in glob.glob("*.eml"):
        email = os.stat(e)
        count = count + 1
        size = size + email.st_size
    return size, count

#def list():
 #   count, size = 0
  #  for e in glob.glob("*.eml"):
   #     email = os.stat(e)
    #    count = count + 1
     #   size = size + email.st_size
    #return size, count

#def retr():

#def dele():
    
#def top():

#def quit():


serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server ready to receive...')
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Data received...")
    command = connectionSocket.recv(2048).decode()
    print("Sending return messge...")

    if command == 'LIST':
        emailList, counter = list()
    elif command == 'STAT':
        size, count = stat()
        output = str(count) + ' ' + str(size)
        connectionSocket.send(output.encode())
    elif command == 'QUIT':
        connectionSocket.close()

connectionSocket.close()

