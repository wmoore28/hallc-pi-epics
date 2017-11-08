#!/usr/bin/env python

import sys
import time
import datetime
import epics

record_pv = epics.PV("C_LASER:DAQ:REC")	    # 0=off, 1=on
speed_pv  = epics.PV("C_LASER:DAQ:SPD")	    # 0=low, 1=high
pwr_a     = epics.PV("C_LASER:DAQ:PWR_A")
pwr_b     = epics.PV("C_LASER:DAQ:PWR_B")

f=open('/data/Newport2936R.dat', 'a', buffering=0)
try:
    while True:
	ts = datetime.datetime.now()
	if record_pv.value == 1:
	    f.write("%s %s %s\n" %(ts, pwr_a.value, pwr_b.value))
	if speed_pv.value == 0:
	    time.sleep(0.2)
except KeyboardInterrupt:
    f.flush()
    f.close()
    sys.exit()
