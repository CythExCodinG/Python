from threading import Thread
import time
def sq_num(num):
  for n in num:
    print(f"Sq of num:{n**2}")
    time.sleep(1)
def cu_num(num):
  for n in num:
    print(f"Cube of num:{n**3}")
    time.sleep(1)
number=[3,2,5,7,6]
# t1=Thread(target=sq_num,args=(number,))
# t2=Thread(target=cu_num,args=(number,))
# s_time=time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# e_time=time.time()
s_time=time.time()
sq_num(number)
cu_num(number)
e_time=time.time()

print(f"Total Execution time is :{e_time-s_time}")