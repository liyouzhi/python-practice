import logging

print("--------------1--------------------")
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

print("--------------2--------------------")
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('except:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

print("----------------3------------------")
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('ERROR:',e)
    finally:
        print('finally....')
main()

print("----------------4------------------")
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('1')
main()
print('END')

print("----------------5------------------")
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')

print("----------------6------------------")
class FooError(ValueError):
    pass

def foo1(s):
    n = int(s)
    if n == 0 :
        raise FooError('invalid value:%s' % s)
    return 10 / n
try:
    foo1('0')
except FooError as e:
    print('FooError!')
print('END')

print("----------------7------------------")
def foo2(s):
    n = int(s)
    if n == 0 :
        raise ValueError('invalid value:%s' % s)
    return 10 / n

def bar2():
    try:
        foo2('0')
    except ValueError as e:
        print('ValueError!')
        raise
try:
    bar2()
except ValueError as e:
    print('main:ValueError!!!')
print('END')

print("----------------8------------------")
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error')
print('END')
