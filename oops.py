class python:
    x=5
y=python()
print(y.x)
    
    
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("Anu",25)
print(p.name)
print(p.age)


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfn(self):
        print("my name is",self.name)
        print("age",self.age)
per=person("akhi",24)
per.myfn()






    