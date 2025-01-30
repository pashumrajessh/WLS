connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the persistent store, dizzy2JDBCStore.'
	cd('/JDBCStores/dizzy2JDBCStore')
	print 'The dizzy2JDBCStore already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createJDBCStore('dizzy2JDBCStore')
cd('/JDBCStores/dizzy2JDBCStore')
cmo.setDataSource(getMBean('/JDBCSystemResources/dizzyworldDS'))
set('PrefixName','migrate')
set('Targets',jarray.array([ObjectName('com.bea:Name=dizzy2 (migratable),Type=MigratableTarget')], ObjectName))
activate()

disconnect()
exit()

