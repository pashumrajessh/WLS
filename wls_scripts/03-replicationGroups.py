connect('system','weblogic', 't3://localhost:7001')

edit()

startEdit(-1,-1,'false')



startEdit(-1,-1,'false')
cd('/Servers/dizzy1')
set('PreferredSecondaryGroup','dizzyRepGroup2')
set('ReplicationGroup','dizzyRepGroup1')
cd('/')
cd('/Servers/dizzy2')
set('PreferredSecondaryGroup','dizzyRepGroup2')
set('ReplicationGroup','dizzyRepGroup1')
cd('/')
cd('/Servers/dizzy3')
set('PreferredSecondaryGroup','dizzyRepGroup1')
set('ReplicationGroup','dizzyRepGroup2')
activate()

disconnect()
exit()
