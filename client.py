# Email Client
# Timothy Leach
# Due 10/07/2019

from socket import *
serverName = 'localhost'
serverPort = 42069
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print('From server: ', modifiedSentence.decode())
clientSocket.close()
