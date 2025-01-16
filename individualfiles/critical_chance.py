import random

def generate_random_numbers(count, start=1, end=100):

    return [random.randint(start, end) for _ in range(count)]

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I've selected some random numbers between 1 and 100.")

    correct_numbers = generate_random_numbers(38)  # You can adjust the count
    print(f"Hint: There are {len(correct_numbers)} possible correct numbers.")

    while True:
        try:
            user_guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess in correct_numbers:
            print("Congratulations! You guessed correctly!")
            break
        else:
            print("Incorrect. Here are all the possible correct answers:")
            print(", ".join(map(str, correct_numbers)))

guess_the_number()
