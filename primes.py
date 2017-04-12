#构建素数数列


#从3开始的奇数序列
def _odd():
    n = 1
    while True:
        n = n + 2
        yield n

#x为n的倍数，返回F，否则返回T
def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

#打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break






