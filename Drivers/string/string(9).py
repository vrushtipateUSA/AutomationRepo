# check specific substring is available in the string and get count of it.
str1 = input("enter any string:")
sub_str2 = input("enter character to check frequency:")
count = 0
for i in str1:
    if i == sub_str2:
        count+=1
print(sub_str2, "occurs", count)


