#!../../bin/linux-x86_64/panasonic
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/panasonic.dbd")
panasonic_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/panasonic.db", "P=C_LASER:, R=DAQ:")

cd "${TOP}/iocBoot/${IOC}"
dbl > /logs/${IOC}.pvlist
iocInit
