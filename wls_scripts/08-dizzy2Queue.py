connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the queue, dizzy2Queue.'
	cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/Queues/dizzy2Queue')
	print 'The dizzy2Queue already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule')
cmo.createQueue('dizzy2Queue')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/Queues/dizzy2Queue')
set('JNDIName','dizzy2Queue')
cd('/JMSSystemResources/dizzyworldClusterJMSModule')
cmo.createSubDeployment('BEA_JMS_MODULE_SUBDEPLOYMENT_dizzyworldJMSServer2')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/JMSResource/dizzyworldClusterJMSModule/Queues/dizzy2Queue')
set('SubDeploymentName','BEA_JMS_MODULE_SUBDEPLOYMENT_dizzyworldJMSServer2')
cd('/JMSSystemResources/dizzyworldClusterJMSModule/SubDeployments/BEA_JMS_MODULE_SUBDEPLOYMENT_dizzyworldJMSServer2')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldJMSServer2,Type=JMSServer')], ObjectName))
activate()

disconnect()
exit()
