units=int(input("enter units"))
if units<=100:
    print("no charge")
elif units<=200:
    unit=units-100
    print("total bill",unit*5)
elif units>200:
    unit=units-200
    print("total bill",500+(unit*10))

