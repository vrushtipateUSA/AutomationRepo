strx = "This is our golden time in our life"
c = strx.count("our")
print(c)

stry= "Trust in your god and your karma"
word_list = stry.split()
print(word_list)
min_word = 0
exp_word = " "
for i in word_list:
    word_len = len(i)
    print(word_len, end=" ")
    if min_word > word_len:
       word_len = min_word
       exp_word = i
    else:
        continue




