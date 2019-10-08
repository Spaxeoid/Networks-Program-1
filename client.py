# Email Client
# Timothy Leach
# Due 10/07/2019

from socket import *
import sys
import random

if len(sys.argv) > 1:
    serverName = int(sys.argv[1])
    serverPort = int(sys.argv[2])
else:
    serverName = 'localhost'
    serverPort = 55555

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    command = input('')
    command = command.upper()
    clientSocket.send(command.encode())
    splitCommand = command.split()

    fromServer = clientSocket.recv(2048).decode()
    if splitCommand[0] == 'RETR':
        fileName = 'TEMP_' + str(random.randint(1, 1000)) + '.eml'
        retrievedEmail = open(fileName, 'x')
        retrievedEmail = open(fileName, 'w')
        retrievedEmail.write(fromServer)
        print("went through if")
    if fromServer == "+OK Adios":
        print(fromServer)
        break
    print(fromServer)
clientSocket.close()
