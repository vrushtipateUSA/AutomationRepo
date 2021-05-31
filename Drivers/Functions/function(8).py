# Write a Python function that accepts a string and
# calculate the number of upper case letters and lower case letters

def string(s):
    upper_case = 0
    lower_case = 0
    for i in s:
        if i.isupper():

        elif i.islower():
            lower_case = lower_case =+ 1
        else:
            pass
        print("Original String : ", s)
        print("No. of Upper case characters : ", "upper_case")
        print("No. of lower case characters : ", lower_case)
string("This is Vrushti Patel")



