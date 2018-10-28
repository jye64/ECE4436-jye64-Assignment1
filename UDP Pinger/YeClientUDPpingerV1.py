'''
Created on Oct 11, 2018

@author: alanye
'''
 
from socket import *
from datetime import datetime
from time import time
from audioop import avg
import statistics

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

counter = 0
request = 200
min = 0.0
max = 0.0
avg = 0.0
total = 0.0
loss = 0
requestTime = [250]   #array to store pings, so that standard deviation can be calculated later on

while (counter<request):
    message = "Ping: "
    startTime = datetime.now()
    try:
        message = message +str(counter) +''+str(datetime.now())
        elapsed = (datetime.now()-startTime).microseconds/1000
        total += elapsed
        requestTime.append(elapsed)
        
        if counter == 0:
            min = elapsed
            max = elapsed
        else:
            if elapsed < min:   # update min if elapsed is smaller than the previous min
                min = elapsed
            else:
                if elapsed > max:   # update max if elapsed is bigger than the previous max
                    max = elapsed
                    
        counter += 1
        clientSocket.sendto(bytes(message, "UTF-8"), (serverName,serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print(modifiedMessage)
        
    except timeout:
        loss += 1
        print('*** Request Time Out.***')


        
avg = total/(request - loss)     # calculations
lossPercent = loss/request*100
stddev = statistics.stdev(requestTime)
    
print('Min RTT is: '+str(min))
print('Max RTT is: '+str(max))
print('Avg RTT is: '+str(avg))
print("Packet loss rate is: "+str(lossPercent))
print('Standard Deviation RTT is: '+str(stddev))

    

            
        
    
