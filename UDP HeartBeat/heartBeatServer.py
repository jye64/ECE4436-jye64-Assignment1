'''
Created on Oct 12, 2018

@author: alanye
'''

from socket import *
import time
from builtins import str

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1',12500))
serverSocket.settimeout(1)
packetLoss = 0 

while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        travelTime = message[2:]
        currentTime = time.time()
        timeElapsed = float(currentTime)-float(travelTime)  #calculate the time difference
        print ("Time Elapsed: "+float(timeElapsed))
       
        
    except timeout:
        print("CLient at "+str(address) + "is offline")
        packetLoss +=1
        serverSocket.settimeout(None)
        
serverSocket.close()


