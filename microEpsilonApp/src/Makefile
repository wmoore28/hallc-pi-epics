TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = microEpsilon

# microEpsilon.dbd will be created and installed
DBD += microEpsilon.dbd

# microEpsilon.dbd will include these files:
microEpsilon_DBD += base.dbd

# microEpsilon_registerRecordDeviceDriver.cpp derives from microEpsilon.dbd
microEpsilon_SRCS += microEpsilon_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
microEpsilon_SRCS_DEFAULT += microEpsilonMain.cpp
microEpsilon_SRCS_vxWorks += -nil-

# Link in the code from our support library
microEpsilon_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

