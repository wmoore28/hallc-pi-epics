#!../../bin/linux-x86_64/pyctl
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/pyctl.dbd")
pyctl_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/pyctl.db", "P=C_LASER:,R=DAQ:")

cd "${TOP}/iocBoot/${IOC}"
dbl > /logs/${IOC}.pvlist
iocInit
