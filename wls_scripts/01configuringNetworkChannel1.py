from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzyworldNetworkChannel1 already exists
try:
	cd('/Servers/dizzy1/NetworkAccessPoints/dizzyworldNetworkChannel1')
	print 'The dizzyworldNetworkChannel1 Network Channel already exists.'
	exit()
except WLSTException:
	pass

print 'Changing to edit mode...'
edit()

startEdit()

cd('/Servers/dizzy1')
cmo.createNetworkAccessPoint('dizzyworldNetworkChannel1')
cd('/Servers/dizzy1/NetworkAccessPoints/dizzyworldNetworkChannel1')
set('Protocol','http')
set('ListenAddress','localhost')
set('ListenPort','9001')
set('PublicAddress','localhost')
set('PublicPort','9001')
set('Enabled','true')
set('HttpEnabledForThisProtocol','true')
set('TunnelingEnabled','false')
set('OutboundEnabled','false')

save()
activate()
disconnect()



exit()
