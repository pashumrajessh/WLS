from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('weblogic','weblogic','t3://localhost:7001')

print 'Changing to edit mode...'
edit()

print 'Changing to the Servers/examplesServer/Log/examplesServer MBean directory...'
cd('Servers')
cd('examplesServer')
cd('Log')
cd('examplesServer')
startEdit()

print 'Setting the FileCount attribute to 8...'
set('FileCount','8')
save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()