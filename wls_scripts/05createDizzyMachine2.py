from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzyMachine2 already exists
try:
	cd('/Machines/dizzyMachine2')
	print 'The dizzyMachine2 already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()


cd('/')
cmo.createMachine('dizzyMachine2')
cd('/Servers/dizzy2')
cmo.setMachine(getMBean('/Machines/dizzyMachine2'))
cd('/Servers/dizzy3')
cmo.setMachine(getMBean('/Machines/dizzyMachine2'))
cd('/Machines/dizzyMachine2/NodeManager/dizzyMachine2')
set('ListenAddress','127.0.0.1')
set('ListenPort','5556')


activate()


disconnect()

print 'End of script, exiting WLST...'
exit()
