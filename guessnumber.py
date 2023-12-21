import random
import math
# random.randint will include end(17) randrange will not include end
#if we do not include start, it will start from 0
top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range) #input is a string

    if top_of_range <= 0:
        print('please type a number larger than 0')
        quit()
else:
    print('Enter a number next time')
    quit()

random_number = random.randint(0,top_of_range)
print(random_number)

while True:
    user_guess = input('Make a guess')

    if user_guess.isdigit():
        user_guess = int(user_guess) #input is a string
    else:
        print('Enter a number next time')
        continue
    
    if user_guess == random_number:
        print('you go it correct')
        break
    else:
        print('you got it incorrect')