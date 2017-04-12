class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value
    
    @property
    def age(self):
        return 2016 - self._birth

class screen(object):

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        if value < 0: 
            raise ValueError('width must >0!')
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an integer!')
        if value < 0: 
            raise ValueError('height must >0!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height






