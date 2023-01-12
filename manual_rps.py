import random


def get_computer_choice():
    sel = ['Rock', 'Paper', 'Scissors']
    com = random.choice(sel)
    return com

def get_user_choice():
    user = input('Rock, Paper, Scissors: ')
    return user

get_computer_choice()
get_user_choice()

def get_winner():
    com = get_computer_choice()
    user = get_user_choice()
    if  com == user: 
        print("It is a tie!")
    elif user == 'Rock' and com == 'Paper':
        print("You lost")
    elif user == 'Scissors' and com == 'Rock':
        print("You lost")
    elif  user == 'Paper' and com == 'Scissors':
        print("You lost")
    else:
        print("You won!")
    

def play():
    print('Rock-Paper-Scissors')
    com = get_computer_choice()
    user = get_user_choice()
    game = get_winner(user, com)
    return

play()

get_winner()
