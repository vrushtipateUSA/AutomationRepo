# Write a Python program to append text to a file and display the text.

with open('fname','w') as myfile:
    myfile.write("This is what it is\n")
    myfile.write("how do you focus\n")
txt = open('fname')
print(txt.read())


