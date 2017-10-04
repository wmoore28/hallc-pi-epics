TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = pyctl

# pyctl.dbd will be created and installed
DBD += pyctl.dbd

# pyctl.dbd will include these files:
pyctl_DBD += base.dbd

# pyctl_registerRecordDeviceDriver.cpp derives from pyctl.dbd
pyctl_SRCS += pyctl_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
pyctl_SRCS_DEFAULT += pyctlMain.cpp
pyctl_SRCS_vxWorks += -nil-

# Finally link IOC to the EPICS Base libraries
pyctl_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

