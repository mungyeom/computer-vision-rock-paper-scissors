import random


def get_computer_choice():
    global computer_choice
    sel = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(sel)
    return computer_choice

get_computer_choice()
print(computer_choice)


def get_user_choice():
    global user_choice
    user_choice = input('Rock, Paper, Scissors: ')
    return user_choice

get_user_choice()
user_choice


def get_winner(computer_choice,user_choice):
    if  user_choice == computer_choice: 
        print("It is a tie!")
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        print("You lost")
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print("You lost")
    elif  user_choice == 'Paper' and computer_choice == 'Scissors':
        print("You lost")
    else:
        print("You won!")
    

def play():
    print('Rock-Paper-Scissors')
    get_computer_choice()
    get_user_choice()
    get_winner(computer_choice, user_choice)
    return

play()

