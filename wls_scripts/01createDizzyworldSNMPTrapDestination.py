from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

print 'Changing to edit mode...'


# Check if Diagnostic Module already exists
try:
	cd('SNMPTrapDestinations/dizzyworldSNMPTrapDestination')
	print 'The dizzyworldSNMPTrapDestination Trap Destination already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()


cd('/SNMPAgent/dizzyworld')
cmo.createSNMPTrapDestination('dizzyworldSNMPTrapDestination')
cd('SNMPTrapDestinations/dizzyworldSNMPTrapDestination')
set('Community','public')
set('Host','localhost')
set('Port','162')

cd('/SNMPAgent/dizzyworld')
set('Enabled','true')

save()
activate()

disconnect()

print 'End of script, exiting WLST...'
exit()
