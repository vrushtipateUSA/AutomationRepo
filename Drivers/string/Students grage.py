Sub1 = int(input("Enter the marks of sub1"))
Sub2 = int(input("Enter the marks of sub2"))
Sub3 = int(input("Enter the marks of sub3"))
Sub4 = int(input("Enter the marks of sub4"))
Sub5 = int(input("Enter the marks of sub5"))

TotalMarks = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
print(TotalMarks)
Per = (TotalMarks/5)
print(Per)
if Per <= 30:
    print("C grade")
elif Per > 40 and Per < 50:
    print("pass with B grade")
elif Per > 50 and Per < 60:
    print("Pass with A Grade")
elif Per > 60:
    print("Pass with A+ grade")
else:
    print("fail")



