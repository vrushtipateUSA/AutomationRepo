# Using while loop and an if statement write a function named name_adder
# which appends all the elements in a list to a new list unless the element is an empty string: "".

lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
new_list=["chili","haldi","salt"]
def name_adder(list):
    i = 0
   # new_list = []
    while i < len(lst1):
        if lst1[i] != "":
            new_list.append(lst1[i])
        i = i+1
    return new_list
var = name_adder(lst1)
print(var)
