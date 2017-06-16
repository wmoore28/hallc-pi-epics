#!../../bin/linux-arm/lakeshore224
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/lakeshore224.dbd")
lakeshore224_registerRecordDeviceDriver(pdbbase)

## Port config
drvAsynSerialPortConfigure("USB0", "/dev/ttyUSB0",0,0,0)
asynSetOption("USB0", -1, "baud", "57600")
asynSetOption("USB0", -1, "bits", "7")
asynSetOption("USB0", -1, "stop", "1")
asynSetOption("USB0", -1, "parity", "odd")
asynSetOption("USB0", -1, "clocal", "Y")
asynSetOption("USB0", -1, "crtscts", "N")
asynOctetSetOutputEos("USB0", "\n")
asynOctetSetInputEos("USB0", "\n")

## Port debugging
asynSetTraceMask("USB0",-1,0x9)
asynSetTraceIOMask("USB0",-1,0x2)

## Load record instances
#dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
#dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/lakeshore224.db", "P=C_LASERDAQ, R=TEMP:, PORT=USB0"


cd "${TOP}/iocBoot/${IOC}"
dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5)
#create_monitor_set("info_settings.req", 30)

