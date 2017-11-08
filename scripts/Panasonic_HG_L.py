#!/usr/bin/env python

import time
import datetime
import serial
#import epics

#data_pv = epics.PV("C_LASER:DAQ:DISPLACEMENT")

ser=serial.Serial('/dev/ttyUSB0',
                  baudrate=115200,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,
                  timeout=2
                  )

print(ser.isOpen) # checking if serial port is open
counter=0
counter1=0
data="\xFF"
data1="\x01"#command to read temperature 2 bytes
data2="\x25"
data3="\xA5\x01"
data4="\x01"
data5="x25/x30/x31/x23/x52/x4d/x44/x2a/x2a/x0d" #measurement value read RMD
data6="x25/x30/x31/x23/x52/x4f/x41/x2a/x2a/x0d"#Alarm status ROA
data7="%01#RMD**\r"
data8="%01#WSP+00002**\r"
data9="%01#RSP**\r"
#ser.close()
f=open('/data/panasonic_2_slow','a')
start = time.time()
#print start
#while (time.time() - start) <= 3.0:
#while counter <= 0:
while True:
    #ser.open()
    #time.sleep(0.2)
    ser.write(data7)# query
    counter +=1
    counter1 +=1
    s=ser.read(18)# reading response 2 bytes
    y=datetime.datetime.now()
    #if counter1 > 300:
    #    print s
    #    counter1=0
    #x=s.encode('hex')# converting to hex
    print s
    #print s.encode('ascii')
#    data_pv.value=s
    f.write("%s %s\n" %(s,y))# writing to file
    #print counter
    
print counter
ser.close()
#f.close()
