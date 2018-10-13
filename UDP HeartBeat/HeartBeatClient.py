'''
Created on Oct 12, 2018

@author: alanye
'''

from socket import *
from datetime import *
import time

serverName = '127.0.0.1'
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) #create a client side socket

seq = 0 # sequence number
print(' ===== UDP Heartbeat Client ====')

while True:
    try:
        currentTime = datetime.now()
        message = str(seq)+"\t"+str(currentTime)
        clientSocket.sendto(bytes(message,'UTF-8'),(serverName,serverPort)) # Attach server name, port to message; send into socket
        seq += 1
        print(message)
        time.sleep(1)
        
    except timeout:
        print("Time out!")
        break

clientSocket.close()
