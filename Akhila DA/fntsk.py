a=int(input("enter first number"))
b=int(input("enter second number"))
def sum1():
    return a+b
print(sum1())

a=[1,2,3,4]
def sum2(x):
    s=0
    for i in x:
        s=s+i
    print(s)
sum2(a)

b=[2,3,4,5]
def mul(x):
    m=1
    for i in x:
        m=m*i
    print(m)
mul(b)

x=int(input("Enter a no."))
def p(y):
    if y==1:
        print("not a prime")
    elif y > 1:
        for i in range(2,y):
            if( y % i==0):
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("prime number")
        
p(x)
            





    
    


    
    

        
    
