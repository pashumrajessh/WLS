connect('system','weblogic', 't3://localhost:7001')

edit()

startEdit(-1,-1,'false')

print 'Deploying the dizzyworldDS to the dizzyworldCluster.'


cd('/JDBCSystemResources/dizzyworldDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))
activate()

disconnect()
exit()
