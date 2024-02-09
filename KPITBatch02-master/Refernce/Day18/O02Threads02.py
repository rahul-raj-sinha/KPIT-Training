
# Asynchronous execution of code......
import time
import threading
st = time.perf_counter()

def doJob():
    print(f"Sleeping for 2 seconds......{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up.......")

thrd1 = threading.Thread(target=doJob, name="t1")
thrd2 = threading.Thread(target=doJob, name="t2")
thrd3 = threading.Thread(target=doJob, name="t3")
thrd4 = threading.Thread(target=doJob, name="t4")
thrd5 = threading.Thread(target=doJob, name="t5")
thrd6 = threading.Thread(target=doJob, name="t6")
thrd7 = threading.Thread(target=doJob, name="t7")
thrd8 = threading.Thread(target=doJob, name="t8")
thrd9 = threading.Thread(target=doJob, name="t9")
thrd10 = threading.Thread(target=doJob, name="t10")


#thread execution
thrd1.start()
thrd2.start()
thrd3.start()
thrd4.start()
thrd5.start()
thrd6.start()
thrd7.start()
thrd8.start()
thrd9.start()
thrd10.start()

thrd1.join()
thrd2.join()
thrd3.join()
thrd4.join()
thrd5.join()
thrd6.join()
thrd7.join()
thrd8.join()
thrd9.join()
thrd10.join()


et = time.perf_counter()
print(f"Completed the job in {round(et - st)} seconds.....")
