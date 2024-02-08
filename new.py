#comprehension method
fruits=["apple","orange","cherry","banana"]
f=[]
for i in fruits:
 if "a" in i:
  f.append(i)
print(f)

fruit=["apple","orange","cherry","banana"]
s=[i for i in fruit if "a" in i ]
print(s)


n=[i for i in range(1,7)]
print(n)

m=[i for i in range(1,11) if i<5]
print(m)

y=[i.upper() for i in fruit]
print(y)




