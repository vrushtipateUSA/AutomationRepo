# Given a two integer numbers return their product and
# if the product is greater than 1000, then return their sum

input_1 = int(input("enter a product value"))
input_2 = int(input("enter a product value"))
product = input_1*input_2
sum= 0
if input_1 and input_2 > 1000:
    print(input_1 + input_2)
else:
    print(product)
