#guess_the_number.py
import random
print("Pick a number between 1 and 10")
num1 = random.randint(1, 10)
user_guess = input(f"What is your guess? ")
user_guess = int(user_guess)
guess_counter = 0
while True:
    guess_counter = guess_counter + 1
    if user_guess == num1:
        print("Correct!")
        break
    elif user_guess > num1:
        print("Too high!")
    else:
        print("Too low!")
    print(f"Your number of guesses is {guess_counter}")
    user_guess = input(f"Pick another number ")
    user_guess = int(user_guess)
print(f"Your final number of guesses is {guess_counter}")
