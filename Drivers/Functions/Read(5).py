# Write a python program to find the longest words.

def longest_word(filename):
    with open('tiku.txt') as char:
        word = char.read().split()
        max_len = len(max(word))
        for word in char:
            if len(word) == max_len:
                print(max_len)










