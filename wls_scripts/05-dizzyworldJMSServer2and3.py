connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of JMS servers, dizzyworldJMSServer2 & dizzyworldJMSServer3.'
	cd('/JMSServers/dizzyworldJMSServer2')
	print 'The dizzyworldJMSServer2 and dizzworldJMSServer3 already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJMSServer('dizzyworldJMSServer2')
cd('/JMSServers/dizzyworldJMSServer2')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy2 (migratable),Type=MigratableTarget')], ObjectName))
cd('/')
cmo.createJMSServer('dizzyworldJMSServer3')
cd('/JMSServers/dizzyworldJMSServer3')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy3,Type=Server')], ObjectName))
cd('/JMSSystemResources/dizzyworldJMSModule')
cd('/')
cmo.createSubDeployment('dizzyworldClusterSubdeployment')
cd('/JMSSystemResources/dizzyworldJMSModule/SubDeployments/dizzyworldClusterSubdeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))
activate()

disconnect()
exit()
