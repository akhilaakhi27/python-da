x=lambda a:a+10
print(x(5))

y=lambda a,b:a+b
print(y(5,7))

z=lambda a,b,c:a+b+c
print(z(2,3,4))

def s(n):
    return  lambda a:a*n
b=s(3)
print(b(2))

def x(a):
    return lambda c:c/a
d=x(2)
print(int(d(8)))

l=[("hello",88),("science",42),("maths",75)]
l.sort(key=lambda y:y[0])
print(l)




