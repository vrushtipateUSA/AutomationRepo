def last(n):
  return n[1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
#print(sort_list_last([(2, 5, 6), (1, 2, 8), (4, 4, 6), (2, 3, 2), (2, 1, 5)]))

def addition(num1,num2):

  return num1 + num2

def multiplitaction():
 print(addition(2, 5)*2)


print(last((2, 5, 6)))
