#尾递归优化/n的接乘

def fact(n):
    return fact_iter(n,1)


def fact_iter(num,product):
    if num == 1:
        return product
    else:
        return fact_iter(num-1,num*product)
