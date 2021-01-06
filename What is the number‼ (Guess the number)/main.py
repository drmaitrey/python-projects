import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = (int(input(f"Guess a number between 1 and {x}: ")))
        
        if guess < random_number:
            print("Excuse me, the guess is lower than the number. Try guessing again! See you next time.")
            
        elif guess > random_number:
            print("Excuse me, the guess is greater than the number. Try guessing again! See you next time.")
            
    print(f"Yay! Congrats; you have guessed the number which was {random_number} correctly!.")
        
guess(10)