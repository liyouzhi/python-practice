from functools import reduce

CHAR_TO_FLOAT = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '.':-1
}

def str2float(s):
    nums = list(map(lambda ch:CHAR_TO_FLOAT[ch],s))
    #print(nums)
    point = 0
    def fn(x,y):
        nonlocal point
        if y == -1:
            point = 1
            #print('遇到.了，返回:')
            return x
        if point == 0:
            z = x * 10 + y
            #print('计算整数部分，返回：',z)
            return z
        else:
            point = point * 10
            #print('point=',point)
            xi = x + y / point
            #print('计算小数部分，返回：',xi)
            return xi 

    return reduce(fn,nums)

print(str2float('123.123'))
print(str2float('123.12'))
print(str2float('0.11134'))
print(str2float('12334'))
print(str2float('1230000'))
print(str2float('012332.3434334'))

