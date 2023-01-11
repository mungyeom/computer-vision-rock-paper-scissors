import random

sel = ['rock', 'scissors', 'paper']

def get_computer_choice():
    com = random.randint(0,2)
    com = sel[com]
    return com

def get_user_choice():
    user = input('rock, scissors, paper: ')
    return user

def get_winner(user, com):
    
    if user == com: 
        print("It is a tie!")
    elif user == 'rock' and com == 'paper':
        print("You lost")
    elif user == 'scissors' and com == 'rock':
        print("You lost")
    elif user == 'paper' and com == 'scissors':
        print("You lost")
    else:
        print("You won!")
    

com = get_computer_choice()
user = get_user_choice()
get_winner(user, com)
