s=input("Enter a word")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    
s="AppLE"#to check count
uc=0
lc=0
for i in s:
  if i.isupper():
    uc+=1
  elif i.islower():
    lc+=1
print("uppercount:",uc)
print("lowercount:",lc)


a=[1,2,3,4,5]
e=0
o=0
for i in a:
    if(i%2)==0:
        e+=1
    elif (i%2)!=0:
        o+=1
print("count of even number",e)
print("count of odd no",o)
        
 



