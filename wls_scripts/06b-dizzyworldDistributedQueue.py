connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the distributed queue, dizzyworldDistributedQueue.'
	cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/UniformDistributedQueues/dizzyworldDistributedQueue')
	print 'The dizzyworldDistributedQueue already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule')
cmo.createUniformDistributedQueue('dizzyworldDistributedQueue')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/UniformDistributedQueues/dizzyworldDistributedQueue')
set('JNDIName','dizzyworldDistributedQueue')
set('LoadBalancingPolicy','Round-Robin')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/UniformDistributedQueues/dizzyworldDistributedQueue')
set('SubDeploymentName','dizzyworldClusterSubdeployment')
activate()

disconnect()
exit()
