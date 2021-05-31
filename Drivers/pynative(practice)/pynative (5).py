# Given a string and an integer number n,
# remove characters from a string starting from zero up to n and return a new string

def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("vrushtipatel", 5))