print 'starting the script ....'
username = 'weblogic'
password = 'weblogic'

connect(username,password,'t3://localhost:7001')

edit()
startEdit()

delete('myJDBCDataSource','JDBCSystemResource')

save()
activate(block="true")
