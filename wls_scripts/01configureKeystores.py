from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

print 'Changing to edit mode...'
edit()

startEdit()

# Configure KeyStores

cd("Targets/dizzy1")

cmo.setKeyStores("CustomIdentityAndJavaStandardTrust")
cmo.setCustomIdentityKeyStoreFileName("dw_identity.jks")
cmo.setCustomIdentityKeyStoreType("JKS")
cmo.setCustomIdentityKeyStorePassPhrase("dwstorepass")
cmo.setJavaStandardTrustKeyStorePassPhrase("changeit")

save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()
