def yhtriangles(max):
    l = [1]
    n = 1
    while n <= max:
        print(l)
        l.append(0)
        l = [l[i-1] + l[i] for i in range(n+1)]
        n = n + 1
    print('END')

def yhtriangles_g():
    l = [1]
    while True:
        yield l 
        l.append(0)
        l = [l[i-1] + l[i] for i in range(len(l))]


