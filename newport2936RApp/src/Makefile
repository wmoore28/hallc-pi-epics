TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = newport2936R

# newport2936R.dbd will be created and installed
DBD += newport2936R.dbd

# newport2936R.dbd will include these files:
newport2936R_DBD += base.dbd
newport2936R_DBD += stream.dbd
newport2936R_DBD += asyn.dbd
newport2936R_DBD += drvAsynSerialPort.dbd

# newport2936R_registerRecordDeviceDriver.cpp derives from newport2936R.dbd
newport2936R_SRCS += newport2936R_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
newport2936R_SRCS_DEFAULT += newport2936RMain.cpp
newport2936R_SRCS_vxWorks += -nil-

# Link in the code from our support library
newport2936R_LIBS += stream
newport2936R_LIBS += asyn
newport2936R_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

