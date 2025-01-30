from java.util import *
from javax.management import *
import javax.management.Attribute

print 'Starting the script .... '

connect('system','weblogic','t3://localhost:7001')

# Check if dizzyworldDS data source already exists
try:
	cd('/JDBCSystemResources/dizzyworldDS')
	print 'The dizzyworldDS data source already exists.'
	exit()
except WLSTException:
	pass


print 'Changing to edit mode...'


edit()
startEdit()

# creating JDBC resources

jdbcSR = create('dizzyworldDS','JDBCSystemResource')
theJDBCResource = jdbcSR.getJDBCResource()

connectionPoolParams = theJDBCResource.getJDBCConnectionPoolParams()
connectionPoolParams.setInitialCapacity(5)
connectionPoolParams.setMaxCapacity(15)
connectionPoolParams.setCapacityIncrement(5)
connectionPoolParams.setTestTableName('SYSTABLES')
connectionPoolParams.setLoginDelaySeconds(1)

dsParams = theJDBCResource.getJDBCDataSourceParams()
dsParams.addJNDIName("dizzyworldDS")
theJDBCResource.setName("dizzyworldDS")

driverParams = theJDBCResource.getJDBCDriverParams()
driverParams.setUrl('jdbc:pointbase:server://localhost:9092/HRDATABASE')
driverParams.setDriverName('com.pointbase.jdbc.jdbcUniversalDriver')
driverProperties = driverParams.getProperties()

proper = driverProperties.createProperty('user')
proper.setName('user')
proper.setValue('PBPUBLIC')

proper1 = driverProperties.createProperty('databaseName')
proper1.setName('databaseName')
proper1.setValue('jdbc:pointbase:server://localhost:9092/HRDATABASE')

driverParams.setPassword('PBPUBLIC')

# targeting the resources to the Managed Server called dizzy1

cd('/')
tgtServer = getMBean("/Servers/dizzy1")
tgtServer.setJavaCompiler("javac")
tgtServer.setListenAddress("localhost")
tgtServer.setListenPort(7003)
tgtServer.setInstrumentStackTraceEnabled(1)


jdbcSR.addTarget(tgtServer)


save()
activate()
disconnect()

print 'End of script, exiting WLST...'
exit()
