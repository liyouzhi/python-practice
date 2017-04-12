def fact(n):
    '''
    a function which can calculate n!

    >>> fact(1)
    1
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact('a')
    Traceback (most recent call last):
        ...
    TypeError: unorderable types: str() < int()
    >>> fact(1.5)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(5)
    120
    >>> fact(100)
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    >>> fact(20)
    2432902008176640000
    '''
    if n < 1 or not isinstance(n,int):
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n-1)

if __name__=='__main__':
    import doctest
    doctest.testmod()
