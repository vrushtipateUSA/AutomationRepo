item1 = int(input("Enter first item price"))
item2 = int(input("Enter second item price"))
item3 = int(input("Enter third item price"))
item4 = int(input("Enter fourth item price"))
item5 = int(input("Enter fifth item price"))

TotalBill = item1 + item2 + item3 + item4 + item5

if TotalBill > 500:
    print("NetAmt", (TotalBill * 20/100) - TotalBill)
else:
    print("No discount")
