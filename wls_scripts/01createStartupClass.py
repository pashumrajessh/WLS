from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

print 'Changing to edit mode...'


# Check if startup class already exists
try:
	cd('/StartupClasses/Executive Offices')
	print 'The startup class already exists.'
	exit()
except WLSTException:
	pass
	
	
print 'Changing to edit mode...'
edit()
startEdit()


cd('/')
cmo.createStartupClass('Executive Offices')
cd('/StartupClasses/Executive Offices')
set('ClassName','Lab09.exercise.startup.BindObjects')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server')], ObjectName))

save()
activate()

disconnect()

print 'End of script, exiting WLST...'
exit()
