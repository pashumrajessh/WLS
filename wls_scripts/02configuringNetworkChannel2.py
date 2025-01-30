from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzyworldNetworkChannel2 already exists
try:
	cd('/Servers/AdminServer/NetworkAccessPoints/dizzyworldNetworkChannel2')
	print 'The dizzyworldNetworkChannel2 Network Channel already exists.'
	exit()
except WLSTException:
	pass

print 'Changing to edit mode...'
edit()

startEdit()

cd('/Servers/AdminServer')
cmo.createNetworkAccessPoint('dizzyworldNetworkChannel2')
cd('/Servers/AdminServer/NetworkAccessPoints/dizzyworldNetworkChannel2')
set('Protocol','http')
set('ListenAddress','localhost')
set('ListenPort','8001')
set('PublicAddress','localhost')
set('PublicPort','8001')
set('Enabled','true')
set('HttpEnabledForThisProtocol','true')
set('TunnelingEnabled','false')
set('OutboundEnabled','false')

save()
activate()
disconnect()



exit()
