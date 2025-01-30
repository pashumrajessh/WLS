#BEFOR GOING TO RUN THIS COMMAND COFIGURE NODE MANAGER

from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('rambabu','rambabu.m','t3://192.168.1.22:7001')


# Check if dizzy2 is already running
try:
        start('server5','Server','t3://192.168.1.22:7001')
	exit()
except WLSTException:
	print 'The Server1 managed server already running.'
	pass




disconnect()

print 'End of script, exiting WLST...'
exit()
