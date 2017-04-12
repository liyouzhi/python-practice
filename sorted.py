from operator import itemgetter

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Zhaopeng',34), ('liyouzhi',98), ('peipei',89)]

def by_name(t):
    return t[0].lower()

#print(by_name(l[0]))

print(sorted(l,key=by_name))
print(sorted(l,key =lambda t:t[0]))
print(sorted(l,key =lambda t:t[0].lower()))
print(sorted(l,key =lambda t:t[1]))
print(sorted(l,key =lambda t:t[1],reverse = True))


print(sorted(l,key =itemgetter(0)))
print(sorted(l,key =itemgetter(1),reverse = True))
