#!/usr/bin/env python

import time
import datetime
import serial
#import epics

record_pv = epics.PV("C_LASER:DAQ:REC")        # 0=off, 1=on
speed_pv  = epics.PV("C_LASER:DAQ:SPD")        # 0=low, 1=high

ser=serial.Serial('/dev/ttyUSB0',
                  baudrate=9600,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,
                  timeout=2
                  )

print(ser.isOpen) 																	# checking if serial port is open
counter=0
data1="\x01"																				#command to read temperature 2 bytes in hex
f=open('/home/pi/Desktop/CTLM2H1_2_slow','a')				# file path and append file
start = time.time()
#while (time.time() - start) <= 3.0:
while True:
    	ser.write(data1)# query
    	counter +=1
    	s=ser.read(2)																	# reading response 2 bytes
    	y=datetime.datetime.now()											#timestamp
    	x=(int(s.encode('hex'),16)-1000)/10						# converting to hex, see CTLM manual
        if record_pv.value==1:
    	   f.write("%s %s\n" %(x,y))									# writing to file
	if speed_pv.value==0:
    	   time.sleep(0.2)
print counter
ser.close()
f.close()
