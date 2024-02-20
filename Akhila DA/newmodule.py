import modules
import math
import random
import datetime

x=datetime.datetime.now()
print(x)
print(x.year)
print(x.time())
print(x.month)
print(x.strftime("%B"))#month
print(x.strftime("%b"))
print(x.strftime("%A"))#day
print(x.strftime("%a"))
print(x.strftime("%S"))
print(x.strftime("%H"))
print(x.strftime("%M"))


a=modules.sum(2,3)
print(a)

print(math.sqrt(25))
print(math.pi)
print(math.factorial(3))

print(math.sin(60))
print(math.cos(60))
print(math.tan(90))

print(math.ceil(1.234))
print(math.floor(1.234))
print(math.degrees(2))
print(math.radians(114))


print(min(1,2,3,4,5))
print(max(1,2,3,4,5))
print(abs(-7))
print(pow(2,5))

print(random.randrange(1,10))
print(random.randint(1,5))
print(random.random())#prints random no b/w 0 and 1

list=[1,"apple",2.5,True]
print(random.choice(list))





























