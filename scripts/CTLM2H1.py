import time
import datetime
import serial
#import epics

ser=serial.Serial('/dev/ttyUSB0',
                  baudrate=9600,
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
data3="\xA5\x00"
data4="\x01"
#ser.close()
f=open('/home/pi/Desktop/Python_code/CTLM2H1_2_slow','w')
start = time.time()
#print start
#while (time.time() - start) <= 3.0:
#while counter <= 16:
while True:
    #ser.open()
    ser.write(data1)# query
    counter +=1
    s=ser.read(2)# reading response 2 bytes
    y=datetime.datetime.now()
    #if counter1 > 300:
    #    print s
    #    counter1=0
    x=(int(s.encode('hex'),16)-1000)/10# converting to hex
    #print s.encode('hex')
    f.write("%s %s\n" %(x,y))# writing to file
    #print counter
    time.sleep(0.2)
print counter
ser.close()
f.close()
