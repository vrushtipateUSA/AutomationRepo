input_str = input("Please provide user input:")
most_repeat_char = ''
repeat_char_len = 0
temp = 1
for i in range(len(input_str) -1):
    if input_str[i] == input_str[i+1]:
        temp += 1
        if temp > repeat_char_len:
            repeat_char_len = temp
            most_repeat_char = input_str[i]
    else:
        temp = 1
        continue

print("repeated char len:", repeat_char_len)
print("repeated char: ", most_repeat_char)