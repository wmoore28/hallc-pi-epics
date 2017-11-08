#!/usr/bin/env python

import sys
import time
import datetime
import serial
import epics

record_pv = epics.PV("C_LASER:DAQ:REC")        # 0=off, 1=on
speed_pv  = epics.PV("C_LASER:DAQ:SPD")        # 0=low, 1=high
data_pv   = epics.PV("C_LASER:DAQ:DISPLACEMENT")

ser=serial.Serial('/dev/ttyUSB0',
                  baudrate=115200,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,
                  timeout=2
                  )

#print(ser.isOpen) 			# checking if serial port is open
data="\xFF"
data1="\x01"				# command to read temperature 2 bytes
data2="\x25"
data3="\xA5\x01"
data4="\x01"
data5="x25/x30/x31/x23/x52/x4d/x44/x2a/x2a/x0d" # measurement value read RMD
data6="x25/x30/x31/x23/x52/x4f/x41/x2a/x2a/x0d" # Alarm status ROA
data7="%01#RMD**\r"
data8="%01#WSP+00002**\r"
data9="%01#RSP**\r"

f=open('/data/Panasonic.dat', 'a', buffering=0)
try:
    while True:
        ser.write(data7)
        s=ser.read(18)
        y=datetime.datetime.now()
        x=s[7:15]				# FIXME: not robust solution
        data_pv.value=x
        if record_pv.value==1:
           f.write("%s %s\n" %(x,y))
        if speed_pv.value==0:
           time.sleep(0.2)
except KeyboardInterrupt:
   ser.close()
   f.flush()
   f.close()
   sys.exit()
