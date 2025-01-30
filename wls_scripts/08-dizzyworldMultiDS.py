connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the multi data source, dizzyworldMultiDS.'
	cd('/JDBCSystemResources/dizzyworldMultiDS/JDBCResource/dizzyworldMultiDS')
	print 'The dizzyworldMultiDS already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJDBCSystemResource('dizzyworldMultiDS')
cd('/JDBCSystemResources/dizzyworldMultiDS/JDBCResource/dizzyworldMultiDS')
set('Name','dizzyworldMultiDS')
cd('/')
cd('/JDBCSystemResources/dizzyworldMultiDS/JDBCResource/dizzyworldMultiDS/JDBCDataSourceParams/dizzyworldMultiDS')
set('JNDINames',jarray.array([String('dizzyworldMultiDS')], String))
set('AlgorithmType','Failover')
set('DataSourceList','dizzyworldDS,dizzyworldDS2')
cd('/')
cd('/JDBCSystemResources/dizzyworldMultiDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))
activate()

disconnect()
exit()
