
# write a decorator that calculates the time taken by a function to execute
import time

def Exection_Time(func):
    def wrapper(sec):
        start_time=time.time()
        func(sec)
        end_time=time.time()
        total_time=end_time-start_time
        print("Total time={}".format(total_time))
    return wrapper

@Exection_Time
def func(sec):
    time.sleep(sec)
    print('function execution complete')

func(3)
