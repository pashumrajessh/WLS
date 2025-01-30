connect('system','weblogic', 't3://localhost:7001')


edit()

startEdit(-1,-1,'false')

cd('/MigratableTargets/dizzy2 (migratable)')
cmo.setUserPreferredServer(getMBean('/Servers/dizzy2'))
set('ConstrainedCandidateServers',jarray.array([ObjectName('com.bea:Name=dizzy1,Type=Server'), ObjectName('com.bea:Name=dizzy2,Type=Server'), ObjectName('com.bea:Name=dizzy3,Type=Server')], ObjectName))
activate()

disconnect()
exit()

