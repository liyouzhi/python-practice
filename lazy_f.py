
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6,7,8,9)
print('f=',f)

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print('f1=',f1)
print('f2=',f2)
print('f3=',f3)

print('f1()=',f1())
print('f2()=',f2())
print('f3()=',f3())

def count2():
    def f(j):
        return j*j
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print('f1=',f1)
print('f2=',f2)
print('f3=',f3)

def count3():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count3()
print('f1=',f1)
print('f2=',f2)
print('f3=',f3)

print('f1()=',f1())
print('f2()=',f2())
print('f3()=',f3())















