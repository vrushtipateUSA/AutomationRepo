def sumnum(Num):
    PreviousNum = 0
    for i in range(Num):
        sum = PreviousNum + i
        print("Current Number", i, "Previous Number ", PreviousNum, " Sum: ", sum)
        PreviousNum = i
print("Printing current and previous number sum in a given range(10)")
sumnum(11)
