# Write a Python program to add a key to a dictionary.

d = {0: 10, 1: 20}
print(d)
d.update({2:30})
print(d)

# Write a Python script to concatenate following dictionaries to create a new one

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Di_new = {}

# one way

dict_new = dict(dic1)
dict_new.update(dic2)
dict_new.update(dic3)
print(dict_new)

# another way

for i in (dic1,dic2,dic3):
    Di_new.update(i)
print(Di_new)
