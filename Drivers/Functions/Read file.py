# Create a file and use the Write mode.

file1 = open('vrushti.txt','w')
file1.write("this is vrushti patel\n")
file1.write("I am trying to find a job\n")
file1.write("I am learning a python language\n")
file1.close()

# Read the text file
file1 = open('vrushti.txt','r')
sample = file1.read()
print(sample)





