# Computer Vision RPS

## Milestone 1: Set up the environment

### Task 1
- In this project, I will use GitHub to track changes toyourcode and save them online in a GitHub repo.

## Milestone 2: Create the computer vision system

### Task 1
- Create an image project model with four different classes: Rock, Scissors, Paper, and Nothing
- Go to Teachable-Machine  to start creating the model. 
- Each class is trained with images of yourself showing each option to the camera. 
- The "Nothing" class represents the lack of option in the image. 
- Remember that the more images you train with, the more accurate the model will be

### Task 2
- Download the model
- Download the model from the "Tensorflow" tab in Teachable-Machine. 
- The model should be named keras_model.h5 and the text file containing the labels should be named labels.txt.
- The files you are downloading contain the structure and the parameters of a deep learning model. 
- They are not files that can be run, and they do not contain anything readable if I look inside. 
- Later, I will load them into your Python application in the next milestone.
- Make sure I push the model and labels to my GitHub repository after committing.

### Task 3
- Begin documenting the experience 
- Now that I have created your model and downloaded it, add documentation to your README file following this guide.

## Milestone 3: Install the dependencies

### Task 1 : Create a new virtual environment - For Users who are on Mac with an M1 Chip
- Are you on a Mac with an M1 chip? If not mark this task as complete and move on to the next task
- Once you installed miniconda. First, create a virtual environment by running the following commands:
- conda create -n tensorflow-env python=3.9
- conda activate tensorflow-env
- conda install pip
- Then, follow the steps from the section that says "arm64: Apple Silicon" from this link .
- Once you get tensorflow for Mac, you will install opencv for Mac by running the following commands:
- conda install -c conda-forge opencv

### Task 2 : Complete the installation of dependencies
- And finally, make sure you install ipykernel by running the following command: pip install ipykernel
- Once you installed everything (regardless of the operating system) create a requirements.txt file by running the following command: pip list > requirements.txt
- This file enables any other user that wants to use your computer to easily install these exact dependencies by running  pip install requirements.txt 

### Task 4 : Check the model works
- Run this file  just to check the model you downloaded is working as expected
- Make sure that you have the correct name for the model, the correct name for the labels, and that the model and this file are in the same folder.

## Milestone 4: Create a Rock -Paper- Scissors game

### Task 1 : Store the user's and the computer's choices
- This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
- Create another file called manual_rps.py that will be used to play the game without the camera.
- You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.
- Create two functions: get_computer_choice and get_user_choice.
- The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.
- The second function will ask the user for an input and return it.

### Task 2: Figure out who won
- Using if-elif-else statements, the script should now choose a winner based on the classic rules of Rock-Paper-Scissors.
- For example, if the computer chooses rock and the user chooses scissors, the computer wins.
- Wrap the code in a function called get_winner and return the winner.
- This function takes two arguments: computer_choice and user_choice.
- If the computer wins, the function should print "You lost", if the user wins, the function should print "You won!", and if it's a tie, the function should print "It is a tie!".

### Task 3: Create a function to simulate the game
- All of the code you've programmed so far relates to one thing: running the game - so you should wrap it all in one function.
- Create and call a new function called play.
- Inside the function you will call all the other three functions you've created (get_computer_choice, get_user_choice, and get_winner)
- Now when you run the code, it should play a game of Rock-Paper-Scissors, and it should print whether the computer or  you won.



