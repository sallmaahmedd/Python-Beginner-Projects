#Number Guessing Game
#Program Generates A Random Number, User Guesses, Program Gives Hints (Lower/Higher) & Tracks Attempts

import random
RandomNumber=random.randint(0,1000)
attemptscounter=0

while True:
    guess=int(input("Enter a random number: "))
    attemptscounter+=1
    if guess>RandomNumber:
        print("Too High!")
        continue
    elif guess<RandomNumber:
        print("Too Low!")
        continue
    elif guess==RandomNumber:
        print("You Got It!")
        print(f"Total Attempts: {attemptscounter}")
        break