"""
This script configures a JDBC data source as a System Module and deploys it
to the server
"""
connect("weblogic","weblogic")
edit()

# Change these names as necessary
dsname="myJDBCDataSource"
server="examplesServer"
cd("Servers/"+server)
target=cmo
cd("../..")

startEdit()
# start creation
print 'Creating JDBCSystemResource with name '+dsname
jdbcSR = create(dsname,"JDBCSystemResource")
theJDBCResource = jdbcSR.getJDBCResource()
theJDBCResource.setName("myJDBCDataSource")

connectionPoolParams = theJDBCResource.getJDBCConnectionPoolParams()
connectionPoolParams.setConnectionReserveTimeoutSeconds(25)
connectionPoolParams.setMaxCapacity(100)
connectionPoolParams.setTestTableName("SYSTABLES")

dsParams = theJDBCResource.getJDBCDataSourceParams()
dsParams.addJndiName("ds.myJDBCDataSource")

driverParams = theJDBCResource.getJDBCDriverParams()
driverParams.setUrl("jdbc:pointbase:server://localhost/demo")
driverParams.setDriverName("com.pointbase.xa.xaDataSource")
# driverParams.setUrl("jdbc:oracle:thin:@my-oracle-server:my-oracle-server-port:my-oracle-sid")
# driverParams.setDriverName("oracle.jdbc.driver.OracleDriver")

driverParams.setPassword("examples")
# driverParams.setLoginDelaySeconds(60)
driverProperties = driverParams.getProperties()

proper = driverProperties.createProperty("user")
#proper.setName("user")
proper.setValue("examples")

proper1 = driverProperties.createProperty("DatabaseName")
#proper1.setName("DatabaseName")
proper1.setValue("jdbc:pointbase:server://localhost/demo")

jdbcSR.addTarget(target)

save()
activate(block="true")

print 'Done configuring the data source'

