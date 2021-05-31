# Write a python program to find the longest words.

def longest_word(india):
    str1 = open("tiku.txt",'r')
    longest_word = ''
    for char in str1:
       if len(char)>len(longest_word):
           longest_word = char
    return(longest_word)