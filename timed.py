import time 
def timeme(func):
    def wrapper(): 
        start = time.time() 
        func()
        time.sleep(2)
        end = time.time() 
        mytime = end-start
        print
        print("Total time", end - start) 
    return wrapper
    
@ timeme
def ontime():
    print('time!')
ontime()