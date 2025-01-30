connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the Dizzyworld JMS resources.'
	cd('/JMSServers/dizzyworldJMSServer')
	print 'The Dizzyworld resources already exist.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')

cd('/')
cmo.createJMSServer('dizzyworldJMSServer')
cd('/JMSServers/dizzyworldJMSServer')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server')], ObjectName))
cd('/')
cmo.createJMSSystemResource('dizzyworldJMSModule')
cd('/JMSSystemResources/dizzyworldJMSModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server')], ObjectName))
cmo.createSubDeployment('dizzyworldSubdeployment')
cd('/JMSSystemResources/dizzyworldJMSModule/SubDeployments/dizzyworldSubdeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldJMSServer,Type=JMSServer')], ObjectName))
cd('/JMSSystemResources/dizzyworldJMSModule/JMSResource/dizzyworldJMSModule')
cmo.createQueue('dizzyworldQueue')
cd('/JMSSystemResources/dizzyworldJMSModule/JMSResource/dizzyworldJMSModule/Queues/dizzyworldQueue')
set('JNDIName','dizzyworldQueue')
set('SubDeploymentName','dizzyworldSubdeployment')
cd('/JMSSystemResources/dizzyworldJMSModule/SubDeployments/dizzyworldSubdeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldJMSServer,Type=JMSServer')], ObjectName))
cd('/JMSSystemResources/dizzyworldJMSModule/JMSResource/dizzyworldJMSModule')
cmo.createTopic('dizzyworldTopic')
cd('/JMSSystemResources/dizzyworldJMSModule/JMSResource/dizzyworldJMSModule/Topics/dizzyworldTopic')
set('JNDIName','dizzyworldTopic')
set('SubDeploymentName','dizzyworldSubdeployment')
cd('/JMSSystemResources/dizzyworldJMSModule/SubDeployments/dizzyworldSubdeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldJMSServer,Type=JMSServer')], ObjectName))
activate()

disconnect()
exit()
