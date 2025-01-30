connect('system','weblogic', 't3://localhost:7001')

edit()

startEdit(-1,-1,'false')


startEdit(-1,-1,'false')
cd('/JMSServers/dizzyworldJMSServer2')
cmo.setPersistentStore(getMBean('/JDBCStores/dizzy2JDBCStore'))
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy2 (migratable),Type=MigratableTarget')], ObjectName))
activate()

disconnect()
exit()
