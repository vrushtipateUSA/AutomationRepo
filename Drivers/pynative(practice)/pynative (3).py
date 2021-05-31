# Given a string, display only those characters
# which are present at an even index number.

inputStr = "pynative"
def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)