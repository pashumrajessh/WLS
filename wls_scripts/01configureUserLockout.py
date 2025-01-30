from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

print 'Changing to edit mode...'
edit()

startEdit()

# Configure KeyStores

cd("SecurityConfiguration/dizzyworld")
cd("DefaultRealm/myrealm")
cd("UserLockoutManager/UserLockoutManager")

cmo.setLockoutEnabled(true)
cmo.setLockoutThreshold(3)
cmo.setLockoutDuration(30)

save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()
