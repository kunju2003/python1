a=int(input("enter number of units"))

if a<=100 :
    print("no charge")
elif a>100 and a<=200 :
    print("total bill",(a-100)*5)
else :
    print("total bill",500+(a-200)*10)