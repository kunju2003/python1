a=int(input("enter your bike price:"))
if a>100000 :
    print("road tax=",a*15/100)
elif a>50000 and a<=100000 :
    print("road tax=",a*10/100)
else :
    print("road tax=",a*5/100)
