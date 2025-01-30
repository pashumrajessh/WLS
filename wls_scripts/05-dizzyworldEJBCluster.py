connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the cluster, dizzyworldEJBCluster.'
	cd('/Clusters/dizzyworldEJBCluster')
	print 'The dizzyworldEJBCluster already exists.'
	exit()
except WLSTException:
	pass
	
edit()

startEdit(-1,-1,'false')

#Script Generation Started By: system

cd('/')
cmo.createServer('dizzy4')
cd('/Servers/dizzy4')
set('ListenAddress','localhost')
set('ListenPort','8001')
cd('/')
cmo.createServer('dizzy5')
cd('/Servers/dizzy5')
set('ListenAddress','localhost')
set('ListenPort','8003')
cd('/')
cmo.createMachine('dizzyMachine3')
cd('/Servers/dizzy4')
cmo.setMachine(getMBean('/Machines/dizzyMachine3'))
cd('/Servers/dizzy5')
cmo.setMachine(getMBean('/Machines/dizzyMachine3'))
cd('/')
cmo.createCluster('dizzyworldEJBCluster')
cd('/Clusters/dizzyworldEJBCluster')
set('MulticastAddress','239.192.0.0')
set('MulticastPort','7055')
cd('/')
cd('/Servers/dizzy4')
cmo.setCluster(getMBean('/Clusters/dizzyworldEJBCluster'))
cd('/')
cd('/Servers/dizzy5')
cmo.setCluster(getMBean('/Clusters/dizzyworldEJBCluster'))
activate()

disconnect()
exit()
