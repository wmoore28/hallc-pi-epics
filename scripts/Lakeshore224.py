#!/usr/bin/env python

import sys
import time
import datetime
import epics

record_pv = epics.PV("C_LASER:DAQ:REC")	    # 0=off, 1=on
speed_pv  = epics.PV("C_LASER:DAQ:SPD")	    # 0=low, 1=high
temp_a    = epics.PV("C_LASER:DAQ:TEMP_A")
temp_b    = epics.PV("C_LASER:DAQ:TEMP_B")
temp_c1   = epics.PV("C_LASER:DAQ:TEMP_C1")
temp_d1   = epics.PV("C_LASER:DAQ:TEMP_D1")

f=open('/data/Lakeshore224.dat', 'a', buffering=0)
try:
    while True:
	ts = datetime.datetime.now()
	if record_pv.value == 1:
	    f.write("%s %s %s %s %s\n" %(ts, 
					temp_a.value,
					temp_b.value,
					temp_c1.value,
					temp_d1.value))
	if speed_pv.value == 0:
	    time.sleep(1.0)
	else:
	    time.sleep(0.2)
except KeyboardInterrupt:
    f.flush()
    f.close()
    sys.exit()
