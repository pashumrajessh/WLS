connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the connection factory, dizzyworldConnectionFactory.'
	cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule')
	print 'The dizzyworldConnectionFactory already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule')
cmo.createConnectionFactory('dizzyworldConnectionFactory')
cd('/')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/ConnectionFactories/dizzyworldConnectionFactory')
set('JNDIName','dizzyworldConnectionFactory')
cd('/')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/ConnectionFactories[dizzyworldConnectionFactory]/dizzyworldClusterJMSModule/SecurityParams/dizzyworldClusterJMSModule')
set('AttachJMSXUserId','false')
cd('/')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/SubDeployments/dizzyworldClusterSubdeployment')
set('Targets',jarray.array([], ObjectName))
cd('/')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/ConnectionFactories/dizzyworldConnectionFactory')
set('SubDeploymentName','dizzyworldClusterSubdeployment')

cd('/')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/ConnectionFactories[dizzyworldConnectionFactory]/dizzyworldClusterJMSModule/LoadBalancingParams/dizzyworldClusterJMSModule')
set('ServerAffinityEnabled','false')

activate()

disconnect()
exit()
