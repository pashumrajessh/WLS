connect('weblogic','weblogic','t3://localhost:7777');
print 'Status',state('AdminServer','Server');
print 'Status',state('MS1','Server');
print 'Status',state('MS2','Server');
disconnect();