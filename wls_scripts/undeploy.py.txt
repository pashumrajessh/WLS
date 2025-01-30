connect("rambabu","rambabu.m")

try:
	print 'Checking for the existence of the Benefits application.'
	cd('/AppDeployments/benefits')
	print 'The Benefits applications will be undeployed.'
	undeploy('benefits')
	exit()
except WLSTException:
	pass

print 'The Benefits application does not exist.'

exit()