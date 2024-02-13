import os
# a=open("hello.txt","x")
a=open("hello.txt","w")
a.write("hello world,welcome to python")
a=open("hello.txt","r")
print(a.read())
a.close()
a=open("hello.txt","a")
a.write("file handling")
a.close()
a=open("hello.txt","r")
print(a.read())
a.close()

# b=open("hi.txt","x")
# os.remove("hi.txt")

os.rmdir("pythonn")





