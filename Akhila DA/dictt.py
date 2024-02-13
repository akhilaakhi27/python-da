a={"name":"anu","age":23}
b={"place":"mannar","id":12345}
c={"course":"mca","clg":"mzc"}

d={}
for i in a,b,c:
    d.update(i)
print(d)


