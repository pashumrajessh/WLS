connect('system','weblogic', 't3://localhost:7001')


try:
	print 'Checking for the existence of the server, proxyServer.'
	cd('/Servers/proxyServer')
	print 'The proxyServer already exists.'
	exit()
except WLSTException:
	pass

edit()

startEdit(-1,-1,'false')


cd('/')
cmo.createServer('proxyServer')
cd('/Servers/proxyServer')
set('ListenAddress','localhost')
set('ListenPort','7009')
activate()

disconnect()
exit()