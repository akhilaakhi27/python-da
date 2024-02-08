a=["apple","orange","grapes","mango","watermelon"]
b=[1,2,3,4,5]

print(len(a))
print(type(a))

print(a[0])
print(a[-1])
print(a[1:4])
print(a[:3])
print(a[2:])

a[3]="pineapple"
print(a)

a.insert(3,"lemon")
print(a)

print(a.append("pineapple"))
print(a)

a.extend(b)
print(a)

a.remove("orange")
print(a)

a.pop(3)
print(a)

for i in a:
 print(i)
 
d=a.copy()
print(d)

g=a+b
print(g)

d.clear()
print(d)

del d
print(d)

fruits=["apple","orange","cherry","banana"]
for i in fruits:
 if a in i:
  print(i)
else:
 print("does not contain a")
  



