import json

class student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return{
            'name': std.name,
            'age': std.age,
            'score':std.score
    }

def dict2student(d):
    return student(d['name'],d['age'],d['score'])


s = student('zp',29,99)
print(json.dumps(s, default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

json_str = json.dumps(s, default=student2dict)
print(json.loads(json_str,object_hook=dict2student))
