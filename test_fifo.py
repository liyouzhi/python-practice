from collections import OrderedDict

class luod(OrderedDict):

    def __init__(self,*args, capacity):
        self._capacity = capacity
        super(luod, self).__init__(*args)

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove', last)
        if containsKey:
            del self[key]
            print('set:', (key,value))
        else:
            print('add:', (key,value))
        OrderedDict.__setitem__(self, key, value)


d = luod([('a',1),('c',2),('d',3)],capacity=4)
print(d)
d['a']=2
print(d)
d['e']=12
print(d)
d['b']=8
print(d)

