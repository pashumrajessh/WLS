username = 'rambabu'
password = 'rambabu.m'
URL='t3://192.168.1.22:7001'
connect(username,password,URL)
domainRuntime()

cd('ServerRuntimes')
 
servers=domainRuntimeService.getServerRuntimes()
for server in servers:
     serverName=server.getName();
     print '**************************************************'
     print '##############      serverName     ###############'
     print '**************************************************'
     print '##### Server State         #####', server.getState()
     print '##### Server ListenAddress #####', server.getListenAddress()
     print '##### Server ListenPort    #####', server.getListenPort()
     print '##### Server Health State    #####', server.getHealthState()