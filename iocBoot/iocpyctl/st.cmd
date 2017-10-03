#!../../bin/linux-arm/pyctl
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
dbl > pv.list
iocInit
