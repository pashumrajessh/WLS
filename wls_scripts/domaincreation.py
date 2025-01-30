readTemplate(r'E:/ak.khan/wlserver_10.3/common/templates/domains/wls.jar')
cd('Servers/AdminServer')
set('ListenAddress','192.168.1.110')
set('ListenPort',7001)
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('welcome1')
setOption('OverwriteDomain','true')
writeDomain(r'E:/ak.khan/user_projects/akdomain')
closeTemplate()
readDomain(r'E:/ak.khan/user_projects/akdomain')

print 'domain created successfully'