import functools

def log(f):
    @functools.wraps(f)
    def wrapper(*args,**kw):
        print('call %s():' % f.__name__)
        return f(*args,**kw)
    return wrapper

@log
def now():
    print('2016-12-22')

now()
print(now.__name__)

def log1(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,f.__name__))
            return f(*args,**kw)
        return wrapper
    return decorator

@log1('execute')
def now1():
    print('Today is 2016-12-22')

now1()
print(now1.__name__)

def log2(f):
    @functools.wraps(f)
    def wrapper(*args,**kw):
        print('begin call %s()' % f.__name__)
        f(*args,**kw)
        print ('end call %s()' % f.__name__)
    return wrapper

@log2
def now2():
    print('TEST NOW2')

now2()
print(now2.__name__)

def log3(text = None):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kw):
            if text == None: 
                print('call %s()' % f.__name__)
            else:
                print(text,f.__name__)
            return f(*args,**kw)
        return wrapper
    return decorator

@log3()
def now3():
    print('test now3')

now3()

def log4(f_or_t):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kw):
            print(text,f.__name__)
            return f(*args,**kw)
        return wrapper
    if isinstance(f_or_t,str) == False:
        text  = 'call'
        return decorator(f_or_t)
    else:
        text = f_or_t
        return decorator

@log4
def now4():
    print('test now4')

@log4('liyouzhi test')
def now5():
    print('test now5')


now4()
now5()
