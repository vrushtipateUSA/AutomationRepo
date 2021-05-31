#  Write a Python program to test whether a passed letter is a vowel or consonant.
input_str = input("please provide your input")
vowel_list = ['a', 'e', 'i', 'o', 'u']

if input_str.lower() not in vowel_list:
    print('consonant')
else:
    print('vowel')
