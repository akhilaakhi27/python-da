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





    
        
