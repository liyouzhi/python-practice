import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    if a==0:
        print('a can not be 0')
        return
    tt = b*b - 4*a*c
    if tt < 0:
        print('There is no solution')
        return
    else:
        x1 = (-b + math.sqrt(tt)) / (2*a)
        x2 = (-b - math.sqrt(tt)) / (2*a)
        return x1,x2

    
