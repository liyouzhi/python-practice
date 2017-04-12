class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    __repr__ = __str__

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('score must between 0-100!')


ZP = Student('Zhao Peng',99)
LYZ = Student('Li You Zhi',59)

ZP.print_score()
LYZ.print_score()

class student(object):
    def __init__(self):
        self.name = 'LY'

    def __call__(self):
        print('My name is %s.' % self.name)

    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


