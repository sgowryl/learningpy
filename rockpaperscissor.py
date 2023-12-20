import random
def play():

    user = input("'r' for rock, 'p' for paper and 's' for scissors")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It is a tie"
    
    if is_win(user, computer):
        return "you won"
    
    return "You lost"
    

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()