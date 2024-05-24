#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

dispaly = []
for letter in chosen_word:
  dispaly += "_"
print(dispaly)

guess = input("Guess a letter: ").lower()
for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")