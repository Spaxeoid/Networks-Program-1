# Email Server
# Timothy Leach
# Due 10/07/2019

from socket import *
import sys
import glob
import os

def stat():
    count = 0
    size = 0
    for e in glob.glob("*.eml"):
        email = os.stat(e)
        count = count + 1
        size = size + email.st_size
    return size, count

def list():
    count = 1
    emailSizes = []
    for e in glob.glob("*.eml"):
        email = os.stat(e)
        count = count + 1
        emailSizes.append(email.st_size)
    return emailSizes, count

def retr(msgNum):
    emailList = glob.glob("*.eml")
    if len(emailList) < int(msgNum):
        output = "-ERR: Index Out of Bounds"
    else:
        with open(emailList[int(msgNum) - 1], 'r') as email:
            emailSize = os.stat(emailList[int(msgNum) - 1])
            emailSize = emailSize.st_size
            output = "+OK " + str(emailSize) + ' octets \n' + email.read() + "\r\n.\r\n"
    return output


def dele(msgNum):
    emailList = glob.glob("*.eml")
    if len(emailList) < int(msgNum):
        output = "-ERR: Index Out of Bounds"
    else:
        os.remove(emailList[int(msgNum) - 1])
        output = '+OK Message Deleted\n'
    return output 
    
def top(linesToRead, msgNum):
    emailList = glob.glob("*.eml")
    if len(emailList) < int(msgNum):
        output = "-ERR: Index Out of Bounds"
    else:
        email = open(emailList[int(msgNum)-1], 'r')
        lineContents = 'Start'
        output = ''
        while lineContents != '\n':
            lineContents = email.readline()
            output = output + lineContents
        for i in range(0, int(linesToRead)):
            output = output + email.readline()
        output = output + "\r\n.\r\n"
    return output


def quit():
    output = "+OK Adios"
    return output


if len(sys.argv) > 1:
    serverPort = int(sys.argv[1])
else:
    serverPort = 55555
killServer = False
while killServer == False:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('Server ready to receive...')
    connectionSocket, addr = serverSocket.accept()
    print("Data received...")
    QUIT = False
    while QUIT == False:
        command = connectionSocket.recv(2048).decode()
        splitCommand = command.split()
        print("Sending return messge...")

        if splitCommand[0] == 'LIST':
            emailSizes, counter = list()
            emailNum = 1
            output = '+OK Mailbox Scan listing follows' 
            for e in emailSizes:
                output = output + '\n ' + str(emailNum) + ' ' + str(e)
                emailNum = emailNum + 1
            output = output + '\r\n.\r\n'
            connectionSocket.send(output.encode())

        elif splitCommand[0] == 'STAT':
            size, count = stat()
            output = str(count) + ' ' + str(size)
            connectionSocket.send(output.encode())

        elif splitCommand[0] == 'DELE':
            output = dele(splitCommand[1])
            connectionSocket.send(output.encode())

        elif splitCommand[0] == 'RETR':
            output = retr(splitCommand[1])
            connectionSocket.send(output.encode())

        elif splitCommand[0] == 'TOP':
            output = top(splitCommand[1], splitCommand[2])
            connectionSocket.send(output.encode())

        elif splitCommand[0] == 'QUIT':
            output = quit()
            connectionSocket.send(output.encode())
            QUIT = True

        elif splitCommand[0] == 'KILLSERVER':
            QUIT = True 
            killServer = True
            output = quit()
            connectionSocket.send(output.encode())

        else:
            connectionSocket.send('Invalid command'.encode())
connectionSocket.close()

