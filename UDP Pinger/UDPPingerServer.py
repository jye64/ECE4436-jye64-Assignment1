'''
Created on Oct 11, 2018

@author: alanye
'''

#UDPPingerServer.py
#We will need the following module to generate randomized lost packets
import random
from socket import *

#create a UDP socket
#Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET,SOCK_DGRAM)
#Assign IP address and port number to socket
serverSocket.bind(('',12000))

while True:
    #generate random number in the range of 0 to 10
    rand = random.randint(0,10)
    #receive the client packet along with the addresss it is coming from
    message, address = serverSocket.recvfrom(1024)
    #capitalize the message from the client
    message = message.upper();
    
    #if rand is less than 3, we consider the packet lost and do not respond if rand<3:
    if rand<3:
        continue
    #otherwise, the server responds
    serverSocket.sendto(message, address)