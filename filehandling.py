# 4 modes for file opening
# read  r mode
# append a mode modification
# write w mode overrite
# x mode-Create file

#1 read mode
f=open("newfile.txt","r")
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for i in f:
#     print(i)
f.close()

#2 append mode
f=open("newfile.txt","a")
# f.write("modify file")
f.close()
f=open("newfile.txt","r")
print(f.read())
f.close()

f=open("newfile.txt","w")
# f.write("welcome to python")
f.close()
f=open("newfile.txt","r")
print(f.read())
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













