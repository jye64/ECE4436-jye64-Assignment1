'''
Created on Oct 12, 2018

@author: alanye
'''

#import socket module
from socket import *
import sys    #in order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)   #SOCK_STREAM indicates a TCP connection

#prepare a server socket

#fill in start
serverPort = 6789
serverSocket.bind(('127.0.0.1',6789))
serverSocket.listen(1)

#fill in end

while True:
    #establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #fill in start   #fill in end
    
    try:
        message =  connectionSocket.recv(1024)  #fill in start   #fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()   #fill in start   #fill in end
        
        #send one HTTP header line into socket
        #fill in start
        connectionSocket.send(bytes('HTTP/1.1 200 OK\nContent-Type: text/html\n\n', "UTF-8"))
        #fill in end
        
        #send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
        
    except IOError:
        #send response message for file not found
        #fill in start
        mes = '404 File Not Found'
        mes.encode()
        connectionSocket.send(mes)
        #fill in end
        
        #close client socket
        #fill in start
        connectionSocket.close()
        #fill in end

serverSocket.close()
sys.exit()  #terminate the program after sending the corresonding data

