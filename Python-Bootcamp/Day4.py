import random
user_choice = int(input("What you want to choose? Type 0 for Rock 1 for paper and 2 for scissor?\n"))

computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice > user_choice:
    print("Younloose")
else:
    print("invalid")