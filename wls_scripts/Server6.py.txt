from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('weblogic','weblogic1','t3://localhost:7001')

# Check if dizzy2 already exists
try:
	cd('/Servers/server7')
	print 'The server2 managed server already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()

cd('/')
cmo.createServer('server7')
cd('/Servers/server7')
set('ListenAddress','127.0.0.1')
set('ListenPort','7008')
activate()

disconnect()

print 'End of script, exiting WLST...'
exit()
