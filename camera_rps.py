import tensorflow.keras
import numpy as np
import cv2
import time
import random
import math


model = tensorflow.keras.models.load_model('keras_model.h5')

cap = cv2.VideoCapture(0)

size =(224, 224)

classes = ['Rock','Paper','Scissors','Nothing']

def get_computer_choice():
    global computer_choice
    sel = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(sel)
    return computer_choice

# def get_winner(computer_choice,user_choice):
#     if  user_choice == computer_choice: 
#         return (0, user_choice, computer_choice)
#     elif user_choice == 'Rock' and computer_choice == 'Paper':
#         return (-1, user_choice, computer_choice)
#     elif user_choice == 'Scissors' and computer_choice == 'Rock':
#         return (-1, user_choice, computer_choice)
#     elif  user_choice == 'Paper' and computer_choice == 'Scissors':
#         return (-1, user_choice, computer_choice)
#     else:
#         return (1, user_choice, computer_choice)

# def computer_wins(n):
#     computer_wins = 0
#     rounds_played = 0
#     wins_necessary = math.ceil(n/2)
#     while computer_wins >= wins_necessary and rounds_played == 5:
#         result, user_choice, computer_choice =  get_winner()
#         if result == 0:
#             rounds_played += 1
#             print("It is a tie! You and computer have both chosen {}. \n" .format(user_choice))
#         elif result == -1:
#             computer_wins += 1
#             rounds_played += 1
#             print("You lost.. You have chosen {} and the computer has chosne {}. \n" .format(user_choice,computer_choice) )



# def user_wins(n):
#     user_wins = 0
#     n = 0
#     wins_necessary = math.ceil(n/2)
#     while user_wins >= wins_necessary:
#         startGame = True 
#         initialTime = time.time()
#         result, user_choice, computer_choice =  get_winner()
#         if result == 0:
#             n += 1
#             print("It is a tie! You and computer have both chosen {}. \n" .format(user_choice))
#         elif result == 1:
#             user_wins += 1
#             n += 1
#             print("You win!! You have chosen {} and the computer has chosne {}. \n" .format(user_choice,computer_choice) )


def get_prediction():
    user_wins = 0
    computer_wins = 0
    stateResult = False
    startGame = False
    img = None  # declare img
    while user_wins < 4 and computer_wins < 4:
        if user_wins == 3:
            print('You won the game!')
            break
        elif computer_wins == 3 :
            print('You lost the game!')
            while True:
                restart = input('Do you want to play again? (y/n) ')
                if restart == 'y':
            # restart the game
                    user_wins = 0
                    computer_wins = 0
                    get_computer_choice()
                    get_prediction()
                elif restart == 'n':
                    print('Thanks for playing!')
                else:
                    print('Invalid input. Please enter y or n.')
                cap.release()
                cv2.destroyAllWindows()
        
        if cap.isOpened():
            ret, img = cap.read()  # update img variable
            if not ret:
                break
            if startGame:
                if stateResult is False:
                    timer = (time.time() - initialTime) 
                    h, w, _ = img.shape
                    cx = h/2
                    img = img[:,200:200+img.shape[0]]
                    img = cv2.flip(img,1)

                    img_input = cv2.resize(img, size)
                    img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)
                    img_input = (img_input.astype(np.float32)/ 127.0) -1
                    img_input = np.expand_dims(img_input, axis=0)

                    prediction = model.predict(img_input)
                    idx = np.argmax(prediction)

                    cv2.putText(img, str(int(timer)), org=(650,30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, \
                    fontScale=0.8, color= (0, 0, 0), thickness=2)

                    cv2.putText(img, text= classes[idx], org=(10,30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, \
                    fontScale=0.8, color= (0, 255, 0), thickness=2)

        
                if timer > 3:
                    stateResult = True
                    timer = 0
                    user_choice = classes[idx]
                    print('You chose' , classes[idx])

                    
                    if user_choice == computer_choice: 
                        print('Tie')
                    elif user_choice == 'Rock' and computer_choice == 'Paper':
                        computer_wins += 1
                        print('Lose')
                        print(computer_wins)
                    elif user_choice == 'Scissors' and computer_choice == 'Rock':
                        computer_wins += 1
                        print('Lose')
                        print(computer_wins)
                    elif user_choice == 'Paper' and computer_choice == 'Scissors':
                        computer_wins += 1
                        print('Lose')
                        print(computer_wins)
                    elif user_choice == 'Nothing':
                        print('Again')
                    else:
                        user_wins += 1
                        print('Win')
                        print(user_wins)

            cv2.imshow('result', img)  # check the image size
            if cv2.waitKey(1) == ord('s'):
                get_computer_choice()
                wins_necessary = 3
                startGame = True 
                initialTime = time.time()
                stateResult = False


get_prediction()
