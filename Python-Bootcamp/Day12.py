# Make function to set difficulty

from random import randint

EASY_TURN = 10
HARD_TURN = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess = int(input("Enter a guess "))
#Set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(f"You had selected {level}")
    if level == "easy":
       return turns = EASY_TURN
    else:
        return turns = HARD_TURN


answer = randint(1, 100)
set_difficulty()


guess = int(input("Enter a guess "))
turns = set_difficulty()
print(f"You have {turns} remaining")
# choosing a random number between 1 and 100

# Let the user guess a num

def check_answer(guess, answer):
    if guess > answer:
        print("guess too high")
    elif guess < answer:
        print("Guess too low")
    else:
        print(f"Correct guess you won!!! corrent answer is {answer}!!!!")
