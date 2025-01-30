readTemplate(r'C:\Oracle\Middleware\wlserver_10.3\common\templates\domains\wls.jar')
cd('Servers/AdminServer')
set('ListenAddress','192.168.1.151')
set('ListenPort',9099)
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('w123456789')
setOption('OverwriteDomain','true')
writeDomain(r'C:\Oracle\Middleware\user_projects\domains\d1')
closeTemplate()
readDomain(r'C:\Oracle\Middleware\user_projects\domains\d1')

print 'domain created successfully'




startServer('AdminServer','d1','t3://192.168.1.151:9099','weblogic','w123456789',r'C:\Oracle\Middleware\user_projects\domains\d1')



print 'AdminServer started successfully'

