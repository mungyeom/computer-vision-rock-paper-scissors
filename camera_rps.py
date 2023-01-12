'''
Replace the hard-coded user guess with the output of the computer vision model. Create a new file called camera_rps.py where you will write the new code.
Create a new function called get_prediction that will return the output of the model you used earlier.
Remember that the output of the model you downloaded is a list of probabilities for each class.
You need to pick the class with the highest probability. 
So, for example, assuming you trained the model in this order: "Rock", "Paper", "Scissors", and "Nothing", if the first element of the list is 0.8, the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that you showed "Rock" to the camera with a confidence of 0.8.
The model can make many predictions at once if given many images. 
In your case you only give it one image at a time. 
That means that the first element in the list returned from the model is a list of probabilities for the four different classes. 
Print the response of the model if you are unclear of this.

'''