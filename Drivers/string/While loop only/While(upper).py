Input_str1 = "sqa tools"

Input_str2 = "python"

list1 = []
while True:
    l = input("enter a char")
    if l:
        list1.append(l.upper())
    else:
        break;

for l in list1:
    print(l)