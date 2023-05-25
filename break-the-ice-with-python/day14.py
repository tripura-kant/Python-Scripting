print('Welcome to my python quiz app')

playing = input('Do you want to play? ')

if playing != "yes":
    quit()
score = 0
print('Lets play')

answer = input('What does HTML stand for? ')

if answer.lower() == "hyper text markup language":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('what is 4 +4 ?')

if answer == "8":
    print("correct")
    score +=1
else:
    print("Incorrect")

print("You got "+ str(score) + "question correct")