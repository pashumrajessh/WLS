from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('weblogic','weblogic','t3://localhost:7001')

print 'Changing to edit mode...'
edit()

print 'Changing to the Servers/examplesServer/SSL/examplesServer MBean directory...'
cd('Servers')
cd('examplesServer')
cd('SSL')
cd('examplesServer')
startEdit()

print 'Setting the Enabled attribute to false...'
set('Enabled','false')
save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()