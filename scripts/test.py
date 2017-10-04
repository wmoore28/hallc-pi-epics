#!/usr/bin/env python

import epics

print epics.caget("C_LASER:DAQ:TEMP_A")
exit()
