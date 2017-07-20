TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = lakeshore224

# lakeshore224.dbd will be created and installed
DBD += lakeshore224.dbd

# lakeshore224.dbd will include these files:
lakeshore224_DBD += base.dbd
lakeshore224_DBD += stream.dbd
lakeshore224_DBD += asyn.dbd
lakeshore224_DBD += drvAsynIPPort.dbd

# lakeshore224_registerRecordDeviceDriver.cpp derives from lakeshore224.dbd
lakeshore224_SRCS += lakeshore224_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
lakeshore224_SRCS_DEFAULT += lakeshore224Main.cpp
lakeshore224_SRCS_vxWorks += -nil-

# Link in the code from our support library
lakeshore224_LIBS += stream
lakeshore224_LIBS += asyn
lakeshore224_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

