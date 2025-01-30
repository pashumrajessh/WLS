from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')


# Check if dizzy2 is already running
try:
        start('dizzy2','Server','t3://localhost:7005')
	exit()
except WLSTException:
	print 'The dizzy2 managed server already running.'
	pass




disconnect()

print 'End of script, exiting WLST...'
exit()
