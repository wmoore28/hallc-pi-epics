#!../../bin/linux-arm/newport2936R
############################################################################
< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/newport2936R.dbd")
newport2936R_registerRecordDeviceDriver(pdbbase)

## Port Config
drvAsynSerialPortConfigure("SER0", "/dev/ttyUSB0", 0,0,0)
asynSetOption("SER0", -1, "baud",  "38400")
asynSetOption("SER0", -1, "bits",  "8")
asynSetOption("SER0", -1, "parity" "none")
asynSetOption("SER0", -1, "stop",  "1")

## Port debugging
#asynSetTraceMask("SER0", -1, 0x9)
#asynSetTraceIOMask("SER0", -1, 0x2)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
#
dbLoadRecords("db/newport2936R.db", "P=C_LASER:,R=DAQ:,PORT=SER0")

cd "${TOP}/iocBoot/${IOC}"
dbl > /logs/${IOC}.pvlist
iocInit

## sequencers
seq poll

## Handle autosave 'commands' contained in loaded databases
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5)
create_monitor_set("info_settings.req", 30)

