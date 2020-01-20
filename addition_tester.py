#addition_tester.py
import random
num1 = random.randint(1, 5)
num2 = random.randint(1, 5)
user_guess = input(f"What is {num1} + {num2}?")
user_guess = int(user_guess)
while True:
    if user_guess == num1 + num2:
        print("Yaay!")
        break
    elif user_guess > num1 + num2:
        print("Too high!")
    else:
        print("Too low!")
    user_guess = input(f"What is {num1} + {num2}?")
    user_guess = int(user_guess)
