
import time
import threading

st = time.perf_counter()

def doJob(secs, tname):
    print(f"Sleeping for {secs} seconds ....{tname}")
    time.sleep(secs)
    print(f'Just woke up.....{tname}')

threads = []

for i in range(10):
    t = threading.Thread(target=doJob, name="t"+str(i), args=[2, 'thread-'+str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()
print(f"completed the task in {et - st} seconds....")
