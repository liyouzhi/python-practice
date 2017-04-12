def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b, = b, a+b
        n = n + 1
    return 'done'

def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b 
        a, b, = b, a+b
        n = n + 1
    return 'done'


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    
    def __getitem__(self,n):
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l



