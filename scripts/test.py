#!/usr/bin/env python

import epics

print epics.caget("C_LASERDAQ:TEMP_A")
exit()
