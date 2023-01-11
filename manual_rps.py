import random

sel = ['rock', 'scissors', 'paper']

def get_computer_choice():
    com = random.randint(0,2)
    com = sel[com]
    return com

def get_user_choice():
    user = input('rock, scissors, paper: ')
    print(user)



