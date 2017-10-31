#!../../bin/linux-x86_64/lakeshore224
############################################################################
< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/lakeshore224.dbd")
lakeshore224_registerRecordDeviceDriver(pdbbase)

## Port config
drvAsynIPPortConfigure("ETH0","129.57.212.48:7777",0,0,0)

## Port debugging
#asynSetTraceMask("ETH0", -1, 0x9)
#asynSetTraceIOMask("ETH0", -1, 0x2)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/lakeshore224.db", "P=C_LASER:, R=DAQ:, PORT=ETH0")

cd "${TOP}/iocBoot/${IOC}"
dbl > /logs/${IOC}.pvlist
iocInit

## Handle autosave 'commands' contained in loaded databases
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5)
create_monitor_set("info_settings.req", 30)

