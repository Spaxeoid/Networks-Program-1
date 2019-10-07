# Email Client
# Timothy Leach
# Due 10/07/2019

from socket import *
import sys
serverName = 'localhost'
serverPort = int(sys.argv[1])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('List: ')
clientSocket.send(sentence.encode())
emailList = []
#count = int(clientSocket.recv(2048).decode())
#print(count)
#for i in range(0, count - 1):
 #   print(i)
  #  emailList.append(clientSocket.recv(2048).decode())
#print(emailList[0])

fromServer = clientSocket.recv(2048).decode()

print('From server: ', fromServer)
clientSocket.close()
