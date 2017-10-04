#!../../bin/linux-arm/microEpsilon
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/microEpsilon.dbd")
microEpsilon_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/microEpsilonCTL.db", "P=C_LASER, R=DAQ3:")

cd "${TOP}/iocBoot/${IOC}"
dbl > /logs/${IOC}.pvlist
iocInit
