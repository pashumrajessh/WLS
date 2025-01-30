from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect("system","weblogic","t3://localhost:7001")

print 'Getting security configuration'
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")

print 'Creating users'
atnr.createUser('joe','weblogic','a manager')
atnr.createUser('ted','weblogic','a manager')
atnr.createUser('mary','weblogic','an employee')
atnr.createUser('albert','weblogic','an employee')

print 'Creating groups'
atnr.createGroup('employees','all of the employees')
atnr.createGroup('managers','all of the managers')

print 'Adding members to groups'
atnr.addMemberToGroup('employees','joe')
atnr.addMemberToGroup('employees','ted')
atnr.addMemberToGroup('employees','mary')
atnr.addMemberToGroup('employees','albert')

atnr.addMemberToGroup('managers','joe')
atnr.addMemberToGroup('managers','ted')

print 'End of script, exiting WLST...'
exit()
