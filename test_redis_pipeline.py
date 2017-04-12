import redis
import time
import threading

conn = redis.Redis()

def trans():
    pipeline = conn.pipeline()
    pipeline.incr('trans:')
    time.sleep(.1)
    pipeline.incr('trans:',-1)
    print(pipeline.execute())
    
if 1:
    for i in range(3):
        threading.Thread(target=trans).start()
    time.sleep(.5)
