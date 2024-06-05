# Make function to set difficulty

from random import randint

EASY_TURN = 10
HARD_TURN = 5



#Set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(f"You had selected {level}")
    if level == "easy":
       return  EASY_TURN
    else:
        return  HARD_TURN



set_difficulty()


guess = int(input("Enter a guess "))

# choosing a random number between 1 and 100

# Let the user guess a num

def check_answer(guess, answer):
    if guess > answer:
        print("guess too high")
    elif guess < answer:
        print("Guess too low")
    else:
        print(f"Correct guess you won!!! corrent answer is {answer}!!!!")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("Enter a guess "))
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()

game()
