# Email Server
# Timothy Leach
# Due 10/07/2019

from socket import *
import sys
import glob

def list():
    emailList = []
    counter = 0
    for e in glob.glob("*.eml"):
        emailList.append(e)
        counter++r
    return emailList, counter


serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server ready to receive...')
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Data received...")
    sentence = connectionSocket.recv(2048).decode()
    capitalizedSentence = sentence.upper()
    print("Sending return messge...")
    emailList, counter = list()
    # connectionSocket.send(capitalizedSentence.encode())
    for e in emailList:
        connectionSocket.send(e.encode())
    #connectionSocket.send(emailList.encode())
    connectionSocket.close()

