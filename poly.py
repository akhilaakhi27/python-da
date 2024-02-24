#polymorphism-many forms
x="hello"
print(len(x))

y=(1,2,3)
print(len(y))

print(type(x))
print(type(y))


#overloading-compile tym operation(eg:+)

def add(datatype,*args):
    if datatype=="int":
        ans=0
    elif datatype=="str":
        ans=" "
    for i in args:
        ans=ans+i
    print(ans)
add("int",5,7)
add("str","hello","world")

#overriding-runtime

class a:
    def fn1(self):
        print("feature 1 of class a")
    def fn2(self):
        print("feature 2 of class a")
class b(a):
    def fn1(self):
        print("modified feature 1")
    def fn3(self):
        print("modified feature 3of class b")
x=b()
x.fn1()
    
    
    






