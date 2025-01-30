connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the data source, dizzyworldDS2.'
	cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2')
	print 'The dizzyworldDS2 already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJDBCSystemResource('dizzyworldDS2')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2')
set('Name','dizzyworldDS2')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDataSourceParams/dizzyworldDS2')
set('JNDINames',jarray.array([String('dizzyworldDS2')], String))
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDriverParams/dizzyworldDS2')
set('Url','jdbc:pointbase:server://localhost:9092/HRDatabase')
set('DriverName','com.pointbase.jdbc.jdbcUniversalDriver')
set('Password','PBPUBLIC')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCConnectionPoolParams/dizzyworldDS2')
set('TestTableName','SQL SELECT COUNT(*) FROM SYSTABLES')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDriverParams/dizzyworldDS2/Properties/dizzyworldDS2')
cmo.createProperty('user')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDriverParams/dizzyworldDS2/Properties/dizzyworldDS2/Properties/user')
set('Value','PBPUBLIC')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDriverParams/dizzyworldDS2/Properties/dizzyworldDS2')
cmo.createProperty('databaseName')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDriverParams/dizzyworldDS2/Properties/dizzyworldDS2/Properties/databaseName')
set('Value','jdbc:pointbase:server://localhost:9092/HRDatabase')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2/JDBCResource/dizzyworldDS2/JDBCDataSourceParams/dizzyworldDS2')
set('GlobalTransactionsProtocol','OnePhaseCommit')
cd('/')
cd('/JDBCSystemResources/dizzyworldDS2')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))
activate()

disconnect()
exit()
