def s():
    print("hello")
s()


#2types-user defined,built in



def fun(t):
    print(t)
x=5
fun(x)
#arbitrary argument-rep by *
def names(*child):
    print("hello"+" "+child[0])
names("Akhi","Saheena","Nithin")

#keyword argument
def names1(child1,child2,child3):
    print("hai"+" "+child1)
names1(child1="Anu",child2="manu",child3="akhi")

#arbitrary keyword argument
def names2(**id):
    print("hello"+" "+id["first"])
names2(first="Akhila",age=24)

a=["apple","orange","grapes"]
def fruit():
    for i in a:
        print(i)
fruit()


def sum1(b):
    return 5+b
print(sum1(3))






    





