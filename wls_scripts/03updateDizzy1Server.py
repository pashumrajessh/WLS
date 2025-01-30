from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if JMS Server exists
try:
	cd('/Servers/dizzy1')
except WLSTException:
	print 'The Managed Server dizzy1 does not exist.'
	exit()

print 'Changing to edit mode...'
edit()
startEdit()

cd('/Servers/dizzy1/SSL/dizzy1')
set('Enabled','true')
set('ListenPort','7004')

activate()

disconnect()

print 'End of script, exiting WLST...'
exit()
