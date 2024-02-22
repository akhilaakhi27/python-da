try:
  x=5
  print(x)  
except NameError:
    print("Define x")
except:
    print("An error occured")
else:
    print("no error")
finally:
    print("sucess")
    
    

a=-1
if a<0:
    raise Exception("no.s less than 0 is not accepted")

    

