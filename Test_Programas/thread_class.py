import threading
import time

# Custom thread class extending Thread
class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 6):
            print(f"MyThread: {i}")
            time.sleep(1)

# Create an instance of MyThread
my_thread = MyThread()

# Start the thread
my_thread.start()

# Wait for the thread to finish
my_thread.join()

print("Thread created by extending Thread class has finished.")
