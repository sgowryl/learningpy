import random

name = input("Type your name ")
print('Welcome ', name , ' to this adventure ')

answer = input("you are on a dead end, which way do you want to go? left or right ").lower()
if answer == 'left':
    answer = input('you come to a river and you can walk around it or swim across, tyoe walk or swim ').lower()
    if answer == 'swim':
        print('you swim across and eaten by an alligator ')
    elif answer == 'walk':
        print("you walked for many miles and ran out of water and you die ")
    else:
        print('Not a valid option')
elif answer == 'right':
    answer = input('you come to a brdige, which looks wobbly, do you want to cross or go back, tyoe cross or back').lower()
    if answer == 'back':
        print('you go back and lose')
    elif answer == 'cross':
        answer = input("you crossed the bridge, do you want to talk to them ").lower()
        if answer == 'yes':
            print('you talk to stranger and win gold, you won')
        elif answer == 'no':
            print("you ignore stranger, you lost")
        else:
            print('Not a valid option')
    else:
        print('Not a valid option')
else:
    print('Not a valid option')