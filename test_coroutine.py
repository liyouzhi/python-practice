
def costomer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[COSTOMER] Consuming %s...' % n)
        r = '200 OK'



def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

def main():
    c = costomer()
    producer(c)

main()
    
