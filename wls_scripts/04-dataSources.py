connect("system", "weblogic", "t3://localhost:7001")

try:
	cd('/JDBCSystemResources/CatalogDS')
	print 'The JDBC Data Source CatalogDS already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJDBCSystemResource('CatalogDS')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS')
set('Name','CatalogDS')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDataSourceParams/CatalogDS')
set('JNDINames',jarray.array([String('CatalogDS')], String))
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDriverParams/CatalogDS')
set('Url','jdbc:pointbase:server://localhost:9092/HRDatabase')
set('DriverName','com.pointbase.jdbc.jdbcUniversalDriver')
set('Password','PBPUBLIC')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCConnectionPoolParams/CatalogDS')
set('TestTableName','SQL SELECT COUNT(*) FROM SYSTABLES')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDriverParams/CatalogDS/Properties/CatalogDS')
cmo.createProperty('user')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDriverParams/CatalogDS/Properties/CatalogDS/Properties/user')
set('Value','PBPUBLIC')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDriverParams/CatalogDS/Properties/CatalogDS')
cmo.createProperty('databaseName')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDriverParams/CatalogDS/Properties/CatalogDS/Properties/databaseName')
set('Value','jdbc:pointbase:server://localhost:9092/HRDatabase')
cd('/JDBCSystemResources/CatalogDS/JDBCResource/CatalogDS/JDBCDataSourceParams/CatalogDS')
set('GlobalTransactionsProtocol','OnePhaseCommit')
cd('/JDBCSystemResources/CatalogDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))


cd('/')

cmo.createJDBCSystemResource('ClientDS')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS')
set('Name','ClientDS')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDataSourceParams/ClientDS')
set('JNDINames',jarray.array([String('ClientDS')], String))
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDriverParams/ClientDS')
set('Url','jdbc:pointbase:server://localhost:9092/HRDatabase')
set('DriverName','com.pointbase.jdbc.jdbcUniversalDriver')
set('Password','PBPUBLIC')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCConnectionPoolParams/ClientDS')
set('TestTableName','SQL SELECT COUNT(*) FROM SYSTABLES')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDriverParams/ClientDS/Properties/ClientDS')
cmo.createProperty('user')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDriverParams/ClientDS/Properties/ClientDS/Properties/user')
set('Value','PBPUBLIC')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDriverParams/ClientDS/Properties/ClientDS')
cmo.createProperty('databaseName')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDriverParams/ClientDS/Properties/ClientDS/Properties/databaseName')
set('Value','jdbc:pointbase:server://localhost:9092/HRDatabase')
cd('/JDBCSystemResources/ClientDS/JDBCResource/ClientDS/JDBCDataSourceParams/ClientDS')
set('GlobalTransactionsProtocol','OnePhaseCommit')
cd('/JDBCSystemResources/ClientDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))
activate()

disconnect()
exit()