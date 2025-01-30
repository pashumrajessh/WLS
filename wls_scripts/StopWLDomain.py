    #====================================  
    # Script File: StopWLDomain.py  
    # This module is for 24x7  Domain****  
    # First phase stops few managed servers of few sites  
    # Second phase will be used for stop remaining servers  
    # Note that Second phase allowed only when you press 'y'  
    # before that you need to Start all the Phase 1 stopped servers.  
    #====================================  
    def conn():  
     try:  
      connect(user, passwd, adminurl)  
     except ConnectionException,e:  
      print '\033[1;31m Unable to find admin server...\033[0m'  
      exit()  
      
    #====================================  
    # Stop all instances of a Cluster   
    #====================================  
    def stopClstr(clstrName):  
     try:  
      shutdown(clstrName,"Cluster")  
      state(clstrName,"Cluster")  
     except Exception, e:  
      print 'Error while shutting down cluster ',e  
      dumpStack()  
      return  
      
    #====================================  
    # All the instances of all Clusters will be down for release  
    #====================================  
    def releaseStop():  
     clstrList=["webclstr1", "webclstr2'..."ejbclstr"]  
     for clstr in clstrList:  
      stopClstr(clstr)   
      
    #====================================  
    # Stop a instances given as parameter   
    #====================================  
    def stopInst(iservr):  
     try:  
      state(str(iservr))  
      shutdown(str(iservr), 'Server',force="true")  
      state(str(iservr))  
     except Exception, e:  
      print iservr, 'is having error in shutting down'  
      pass  
      
    #====================================  
    # Regular Rstart is 24x7 supported for :SITE1, SITE2, SITE3  
    #====================================  
    def regularStop():  
     clstrList=["non247clstr1", "non247clstr2"]  
     for clstr in clstrList:  
      stopClstr(clstr)   
     servrList=servrList=["app1","app2","app3"... "web1","web2"] #sitewise list of servers need to stop  
     for inst in servrList:  
      stopInst(inst)  
     print 'Now, please start the instances exclude the phase 2 instances ...'  
     phase2=raw_input("Want to proceed for Phase 2...(y/n)")  
     if phase2 == 'y':  
      serverList=["app4","web3"...] # remaining Managed Servers to stop after phase servers UP n Running  
      for inst in serverList:  
       stopInst(inst)  
      
    #====================================  
    # Exiting the script  
    #====================================  
    def quit():  
     disconnect()  
     exit()  
      
    #====================================  
    # The main script starts here...  
    #====================================  
    if __name__ == "main":  
     conn()  
     print ' 1. Regular Stop (24x7)\n 2. Release Stop\n 0. Quit\n'  
     sAns=raw_input('Enter your choice: ')  
     if int(sAns) == 1:  
     regularStop()  
     elif int(sAns) == 2:  
     releaseStop()  
     elif int(sAns)== 0:  
     quit()  
     else:  
     print 'Warning: Invalid option...'  
     exit()  
     print 'Finally stopping admin now...'  
     shutdown()  
      
    #========WLST=BY=EXAMPLES==============  
