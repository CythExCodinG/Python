from threading import *
import time
s=Semaphore(2)
def wish(name,age):
  for i in range(2):
    s.acquire()
    print(f"{name}'s age is {age}")
    time.sleep(5)
    s.release()
t1=Thread(target=wish,args=("Rohit",4,))
t1.start()
t2=Thread(target=wish,args=("Rushabh",4,))
t2.start()
t3=Thread(target=wish,args=("Atharva",4,))
t3.start()
t4=Thread(target=wish,args=("Sahil",4,))
t4.start()