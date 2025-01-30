connect('weblogic','weblogic1','t3://192.168.1.151:7001')


try:
	print 'Checking for the existence of the cluster, dizzyworldCluster.'
	cd('Clusters/dizzyworldCluster')
	print 'The dizzyworldCluster already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')

cd('/')
cmo.createCluster('dizzyworldCluster')
cd('/Clusters/dizzyworldCluster')
set('MulticastAddress','239.192.0.0')
set('MulticastPort','7050')
activate()
disconnect()
exit()
