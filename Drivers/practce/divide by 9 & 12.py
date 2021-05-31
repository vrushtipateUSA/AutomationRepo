number = int(input(" Please Enter any Positive Integer : "))

if((number % 9 == 0) and (number % 12 == 0)):
    print("Given Number is Divisible by 9 and 12")
else:
    print("Given Number is Not Divisible by 9 and 12")