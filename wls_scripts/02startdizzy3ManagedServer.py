from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzy3 is already running

try:
        start('dizzy3','Server','t3://localhost:7007')
	exit()
except WLSTException:
	print 'The dizzy3 managed server already running.'
	pass
	

disconnect()

print 'End of script, exiting WLST...'
exit()
