#!/usr/bin/env python

import sys
import time
import epics

record_pv = epics.PV("C_LASER:DAQ:REC")		# 0=off, 1=on
speed_pv  = epics.PV("C_LASER:DAQ:SPD")		# 0=low, 1=high

try:
    while True:
        if record_pv.value:
            print "Recording (" + speed_pv.enum_strs[speed_pv.value] + ")"
        else:
            print "Stopped (" + speed_pv.enum_strs[speed_pv.value] + ")"

        if speed_pv.value:
            delay = 1
        else:
            delay = 5

        time.sleep(delay)

except KeyboardInterrupt:
    print
    sys.exit()
