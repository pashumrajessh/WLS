print 'Connecting to Server'
connect('weblogic','welcome1','t3://192.168.1.110:7001')
appname= 'benefits'
applocation=r'D:\softwares\WLS-A11-91-01-labss\Lab08\exercise\applications\benefits.war'
print 'deploying Application'
deploy(appname,applocation,targets='AdminServer')
print 'Deployment completed'
exit()