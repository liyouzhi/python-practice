import redis
import time
import threading

conn = redis.Redis()

def notrans():
    print(conn.incr('notrans:'))
    time.sleep(.1)
    conn.incr('notrans:',-1)

if 1:
    for i in range(3):
        threading.Thread(target=notrans).start()
    time.sleep(.5)
