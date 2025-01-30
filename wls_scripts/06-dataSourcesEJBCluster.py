connect("system", "weblogic", "t3://localhost:7001")

edit()
startEdit()

cd('/JDBCSystemResources/CatalogDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldEJBCluster,Type=Cluster')], ObjectName))


cd('/')

cd('/JDBCSystemResources/ClientDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldEJBCluster,Type=Cluster')], ObjectName))
activate()

disconnect()
exit()