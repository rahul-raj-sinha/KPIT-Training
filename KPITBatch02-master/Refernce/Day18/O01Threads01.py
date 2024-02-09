
# synchronous Execution of code
import time
st = time.perf_counter()

def doJob():
    print("Sleeping for 2 secs......")
    time.sleep(2)
    print("Just woke up......")
 
doJob()
doJob()

et = time.perf_counter()
print(f"Completed the job in {round(et - st, 2)} seconds.....")

import os
print(os.cpu_count())
