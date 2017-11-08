TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = panasonic

# panasonic.dbd will be created and installed
DBD += panasonic.dbd

# panasonic.dbd will include these files:
panasonic_DBD += base.dbd

# panasonic_registerRecordDeviceDriver.cpp derives from panasonic.dbd
panasonic_SRCS += panasonic_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
panasonic_SRCS_DEFAULT += panasonicMain.cpp
panasonic_SRCS_vxWorks += -nil-

# Finally link IOC to the EPICS Base libraries
panasonic_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

