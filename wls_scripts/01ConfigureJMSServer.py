from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzyworldJMSServer JMS Server already exists
try:
	cd('/JMSServers/dizzyworldJMSServer')
	print 'The dizzyworldJMSServer JMS Server already exists.'
	exit()
except WLSTException:
	pass


print 'Changing to edit mode...'
edit()

startEdit()

# creating JMS Server


cd('/')
cmo.createJMSServer('dizzyworldJMSServer')
cd('/JMSServers/dizzyworldJMSServer')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server')], ObjectName))


save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()
