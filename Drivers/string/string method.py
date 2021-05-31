# To remove the spaces we use Strip method.

stra = "This is a good time for learning"
print(stra)
print(stra.strip())

# Title.
print(stra.title())
print(stra.istitle())

# Split method it is used for seperate the words like in each words section.
# Example: ['This', 'is', 'a', 'good', 'time', 'for', 'learning']

print(stra.split())

strb = "Vrushti is brilliant girl"
print(strb)
print(strb.split())

strc = "Lord Krishna is Great"
print(len(strc))

strd = "II love my country Indiaa"
print(len(strd))
world_list = strd.split(" ")
print(world_list)
max_len = 0
exp_word = " "
for i in world_list:
       word_len = len(i)
       print(word_len, i)
       if word_len > max_len:
          max_len = word_len
          exp_word= i
       else:
           continue
           
           
       
       





    










