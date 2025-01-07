import random

possible_answers = list(range(1, 101))

correct_answers = random.sample(possible_answers, 30)

print(correct_answers)

guess = int(input("Guess a number between 1 and 100: ")) 

if guess not in correct_answers:
    print("Incorrect!")
else:
    print("Your guess is correct! You get a critical hit!")
