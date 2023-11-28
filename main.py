#from getpass import getpass as input
import emoji
from emoji import emojize
import random
print("Welcome to Guess the Number Totally Random One-Million-to-One.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's start the game!")
#import random
attempt = 1
Num = random.randint(1,1000000)
#print()

while True: 
  user_guess = int(input("Pick a number between 1 and 1000000: "))
  if user_guess < Num:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > Num:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == Num:
    print("You are a winner!")
    print(emojize(":smiling_face_with_sunglasses:"))
    break 
    exit()
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")





