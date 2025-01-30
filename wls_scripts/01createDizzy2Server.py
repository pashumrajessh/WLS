from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzy2 already exists
try:
	cd('/Servers/dizzy2')
	print 'The dizzy2 managed server already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()

cd('/')
cmo.createServer('dizzy2')
cd('/Servers/dizzy2')
set('ListenAddress','127.0.0.1')
set('ListenPort','7005')
cd('/Servers/dizzy2/SSL/dizzy2')
set('Enabled','true')
set('ListenPort','7006')
activate()

disconnect()

print 'End of script, exiting WLST...'
exit()
