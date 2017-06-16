TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += lakeshore224Support

# Compile and add the code to the support library
lakeshore224Support_SRCS += xxxRecord.c
lakeshore224Support_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
# This is required for Windows DLL builds.
lakeshore224Support_SRCS += dbSubExample.c
lakeshore224Support_SRCS += lakeshore224Hello.c
lakeshore224Support_SRCS += initTrace.c

lakeshore224Support_LIBS += $(EPICS_BASE_IOC_LIBS)


# Build the IOC application
PROD_IOC = lakeshore224

# lakeshore224.dbd will be created and installed
DBD += lakeshore224.dbd

# lakeshore224.dbd will include these files:
lakeshore224_DBD += base.dbd
lakeshore224_DBD += xxxSupport.dbd
lakeshore224_DBD += dbSubExample.dbd
lakeshore224_DBD += lakeshore224Hello.dbd
lakeshore224_DBD += initTrace.dbd

# lakeshore224_registerRecordDeviceDriver.cpp derives from lakeshore224.dbd
lakeshore224_SRCS += lakeshore224_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
lakeshore224_SRCS_DEFAULT += lakeshore224Main.cpp
lakeshore224_SRCS_vxWorks += -nil-

# Link in the code from our support library
lakeshore224_LIBS += lakeshore224Support

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into lakeshore224Support
    sncExample_SNCFLAGS += +r
    lakeshore224_DBD += sncExample.dbd
    # A .stt sequence program is *not* pre-processed:
    lakeshore224Support_SRCS += sncExample.stt
    lakeshore224Support_LIBS += seq pv
    lakeshore224_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    # A .st sequence program *is* pre-processed:
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
lakeshore224_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

