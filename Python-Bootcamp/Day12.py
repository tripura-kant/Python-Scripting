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






# guess = int(input("Enter a guess "))

# choosing a random number between 1 and 100

# Let the user guess a num

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("Enter a guess "))
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
