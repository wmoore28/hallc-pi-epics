import time
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
f=open('/home/epics/test','w')
start = time.time()
#print start
while (time.time() - start) <= 5.0:
#while counter <= 16:
#while True:
    #ser.open()
    ser.write(data1)# query
    counter +=1
    s=ser.read(2)# reading response 2 bytes
    #if counter1 > 300:
    #    print s
    #    counter1=0
    x=s.encode('hex')# converting to hex
    #print s.encode('hex')
    #f.write("%s\n" %(x))# writing to file
    #print counter
    #time.sleep(0.0028)
print counter
ser.close()
f.close()

