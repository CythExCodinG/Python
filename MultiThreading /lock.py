#the standard lock object does not care which thread is currently holding the lock if the lock is beign hold by one thread and another 
#thread want it to acquire the lock it will be blocked even if it the same thread


# Solution
# Reentrant
# At a time only one thread <=(both lock has common thing)
from threading import *
import time 
l=RLock()
def fact(n):
  l.acquire()
  if n==0:
    res=1
    return res
  else:
    res=n*fact(n-1)
    l.release()
    return res
def show(n):
  print("Factorial of ",n," is ",fact(n))
  
t1=Thread(target=show,args=(5,))
t1.start()

t2=Thread(target=show,args=(6,))
t2.start()

