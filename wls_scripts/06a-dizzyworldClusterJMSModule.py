connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the JMS system module, dizzyworldClusterJMSModule.'
	cd('/JMSSystemResources/dizzyworldClusterJMSModule')
	print 'The dizzyworldClusterJMSModule already exists.'
	exit()
except WLSTException:
	pass


edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJMSSystemResource('dizzyworldClusterJMSModule')
cd('/JMSSystemResources/dizzyworldClusterJMSModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))
cmo.createSubDeployment('dizzyworldClusterSubdeployment')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/SubDeployments/dizzyworldClusterSubdeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldCluster,Type=Cluster')], ObjectName))

activate()

disconnect()
exit()

