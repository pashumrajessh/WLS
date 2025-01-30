from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('rambabu','rambabu.m','t3://192.168.1.22:7001')

# Check if dizzyMachine1 already exists
try:
	cd('/Machines/dizzyMachine1')
	print 'The dizzyMachine1 already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()

cd('/')
cmo.createMachine('dizzyMachine1')
cd('/Servers/server5')
cmo.setMachine(getMBean('/Machines/dizzyMachine1'))
cd('/Machines/dizzyMachine1/NodeManager/dizzyMachine1')
set('ListenAddress','127.0.0.1')
set('ListenPort','5555')

activate()


disconnect()

print 'End of script, exiting WLST...'
exit()
