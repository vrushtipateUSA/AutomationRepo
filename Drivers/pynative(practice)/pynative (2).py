# Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous number

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum, " Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(11)
