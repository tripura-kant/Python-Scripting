#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
end_of_game =  False

print(f'Pssst, the solution is {chosen_word}.')
lives = 6
display = []
for letter in chosen_word:
  display += "_"
print(display)

while not end_of_game:
  guess = input("Guess a letter").lower

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


guess = input("Guess a letter: ").lower()


for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter

if "_" not in display:
  end_of_game = True
  print("You won")

if guess not in chosen_word:
  lives -= 1
  if lives == 0:
    end_of_game = True
    print("End of game")

print(display)