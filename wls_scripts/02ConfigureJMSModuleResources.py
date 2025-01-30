from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzyworldModule JMS Module already exists
try:
	cd('/JMSSystemResources/dizzyworldModule')
	print 'The dizzyworldModule JMS Module already exists.'
	exit()
except WLSTException:
	pass


print 'Changing to edit mode...'
edit()

startEdit()

# creating JMS Server


cd('/')
cmo.createJMSSystemResource('dizzyworldModule','dizzyworldModule-jms.xml')
cd('/JMSSystemResources/dizzyworldModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server')], ObjectName))
cmo.createSubDeployment('dizzy1SubDeployment')
cd('/JMSSystemResources/dizzyworldModule/SubDeployments/dizzy1SubDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server'), ObjectName('com.bea:Name=dizzyworldJMSServer,Type=JMSServer')], ObjectName))
cd('/JMSSystemResources/dizzyworldModule/JMSResource/dizzyworldModule')
cmo.createQueue('dizzyworldQueue')
cd('/JMSSystemResources/dizzyworldModule/JMSResource/dizzyworldModule/Queues/dizzyworldQueue')
set('JNDIName','dizzyworldQueue')
set('SubDeploymentName','dizzy1SubDeployment')
cd('/JMSSystemResources/dizzyworldModule/SubDeployments/dizzy1SubDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldJMSServer,Type=JMSServer')], ObjectName))
cd('/JMSSystemResources/dizzyworldModule/JMSResource/dizzyworldModule')
cmo.createTopic('dizzyworldTopic')
cd('/JMSSystemResources/dizzyworldModule/JMSResource/dizzyworldModule/Topics/dizzyworldTopic')
set('JNDIName','dizzyworldTopic')
set('SubDeploymentName','dizzy1SubDeployment')
cd('/JMSSystemResources/dizzyworldModule/SubDeployments/dizzy1SubDeployment')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzyworldJMSServer,Type=JMSServer')], ObjectName))



save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()
