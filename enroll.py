
def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

def person(name,age,**other):
    print('name:',name,'age:',age,'other',other)

def person2(name,age,*,job,city):
    print(name,age,job,city)

def person3(name,age,*other,job,city='beijing'):
    print(name,age,other,job,city)

