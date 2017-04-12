Loop_Count = 3

def list2map(l):
    s = {}
    for x in l:
        s[x] = x*2
    return s

def list2(l):
    return [2*x for x in l]

def map2(l):
    return {x:2*x for x in l }

def gen_list(i):
    l = [2*(i+j)-1 for j in range(i)]
    return l 

def main():
    l = [1,3,5,7,9]
    x = list2map(l)
    y = list2(l)
    z = map2(l)
    
    print(x)
    print(y)
    print(z)

    for i in range(Loop_Count):
        l = gen_list(i+1)
        ret = map2(l)
        print(ret)

main()
