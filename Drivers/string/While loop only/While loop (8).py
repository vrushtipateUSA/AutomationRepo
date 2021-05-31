# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.

num = 0
tot = 0
while True:

    user_input = input("Enter a number :")
    if user_input == "done":
        break

    else:

        try :
            num1 = float(user_input)
        except:
            print('Invailed Input')
            continue
        num = num+1
        tot = tot + num1
print ('all done')
print (tot,num,tot/num)

