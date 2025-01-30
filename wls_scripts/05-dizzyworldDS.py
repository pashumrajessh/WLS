connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the data source, dizzyworldDS.'
	cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS')
	print 'The dizzyworldDS already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJDBCSystemResource('dizzyworldDS')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS')
set('Name','dizzyworldDS')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDataSourceParams/dizzyworldDS')
set('JNDINames',jarray.array([String('dizzyworldDS')], String))
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDriverParams/dizzyworldDS')
set('Url','jdbc:pointbase:server://localhost:9092/HRDatabase')
set('DriverName','com.pointbase.jdbc.jdbcUniversalDriver')
set('Password','PBPUBLIC')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCConnectionPoolParams/dizzyworldDS')
set('TestTableName','SQL SELECT COUNT(*) FROM SYSTABLES')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDriverParams/dizzyworldDS/Properties/dizzyworldDS')
cmo.createProperty('user')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDriverParams/dizzyworldDS/Properties/dizzyworldDS/Properties/user')
set('Value','PBPUBLIC')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDriverParams/dizzyworldDS/Properties/dizzyworldDS')
cmo.createProperty('databaseName')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDriverParams/dizzyworldDS/Properties/dizzyworldDS/Properties/databaseName')
set('Value','jdbc:pointbase:server://localhost:9092/HRDatabase')
cd('/JDBCSystemResources/dizzyworldDS/JDBCResource/dizzyworldDS/JDBCDataSourceParams/dizzyworldDS')
set('GlobalTransactionsProtocol','OnePhaseCommit')
cd('/JDBCSystemResources/dizzyworldDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server')], ObjectName))
activate()

disconnect()
exit()
