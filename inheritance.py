class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("name",self.name)
        print("age",self.age)
class student(person):
    pass
obj=student("akhi",23)
obj.myfun()

#Types of inheritnce
#1 single-single parent single child
#2 multiple-multiple parent single child
#3 multilevel-one parent class has one derived class it has one child class
#4 hierarchical-same parent class more than 1 child class
#5 hybrid-multiple inheritance

class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self):
        print("the",self.name,self.sound)
class cat(animal):
    pass
s=cat("cat","meow")
class dog(animal):
    pass
S=dog("dog","bark")
s.speak()
S.speak()

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def fun(self):
        print(self.name,"has a salary of",self.salary)
class manager(employee):
    pass
c=manager("Ramesh",50000)
class receptionist(employee):
    pass
C=receptionist("Hari",20000)
c.fun()
C.fun()





    
        
