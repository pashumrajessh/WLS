
from java.util import *
from javax.management import *
import javax.management.Attribute


print 'Starting the Deployment Script for Timeoff.war....'

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')



print 'Changing to Server Configuration mode...'
serverConfig()

role=cmo.getSecurityConfiguration().getDefaultRealm().lookupRoleMapper("DefaultRoleMapper")

print 'Adding the directory role to the timeoff application with the url pattern restriction of /managers/*'

role.createRole('type=<url>, application=timeoff, contextPath=/timeoff, uri=/managers/*','director','Grp(managers)')

disconnect()

print 'End of script, exiting WLST...'
exit()

