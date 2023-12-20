import random

def guess(x):
    random_number = random.randint(1,x)
    #for loop for guessing the number
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print("sorry, guess is too low")
        elif guess> random_number:
            print("sorryr, guess is too high")
    print("yay congrats")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L). or correct(C)").lower()
        if feedback == 'h':
            guess = guess - 1
        elif feedback == 'l':
            guess = guess + 1
        
    print('yay the computer guessed your number {guess} correctly')
computer_guess(10)


