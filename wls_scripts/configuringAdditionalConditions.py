#------------------------------------------------------------------------------
#  Name: WLSLab10Solution.py
#  Author: BEA Systems --> Education
#  Last Modified: 10/13/05
#    Description: This Python script creates a lab 10 environment solution for WLS F2. 
#                 
#  Usage (Note: from CMD prompt run setWLSEnv.cmd first) then: 
#      
#      java weblogic.WLST <WLST_script> 
#
#
#
#  Version: 1.0     
#------------------------------------------------------------------------------

from java.util import *
from javax.management import *
import javax.management.Attribute


print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

role=cmo.getSecurityConfiguration().getDefaultRealm().lookupRoleMapper("DefaultRoleMapper")

print 'Adding the specified day of the month condition to the director role'

role.setRoleExpression('type=<url>, application=timeoff, contextPath=/timeoff, uri=/managers/*','director','Grp(managers)&?weblogic.entitlement.rules.IsDayOfMonth(13,GMT+1:00)')

disconnect()

print 'End of script, exiting WLST...'
exit()

