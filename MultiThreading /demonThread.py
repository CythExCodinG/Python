from threading import Thread
import time
def display():
  print("HI")
t1=Thread(target=display)
t1.setDaemon=True
t1.start()
