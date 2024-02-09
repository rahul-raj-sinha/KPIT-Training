
import time
import threading
import concurrent.futures

st = time.perf_counter()


def doJob(secs):
    print(f"Sleeping for {secs} seconds..... {threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up......{threading.current_thread().name}")
    return "hello"


with concurrent.futures.ThreadPoolExecutor() as executor:
   secs = [6, 5, 4 ,3, 2, 1]
   results = executor.map(doJob, secs)

   for res in results:
       print(res)

et = time.perf_counter()
print(f"completed task in {et - st} seconds......")