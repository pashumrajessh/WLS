from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzy3 already exists
try:
	cd('/Servers/dizzy3')
	print 'The dizzy3 managed server already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()

cd('/')
cmo.createServer('dizzy3')
cd('/Servers/dizzy3')
set('ListenAddress','127.0.0.1')
set('ListenPort','7007')
cd('/Servers/dizzy3/SSL/dizzy3')
set('Enabled','true')
set('ListenPort','7008')
activate()

disconnect()

print 'End of script, exiting WLST...'
exit()
