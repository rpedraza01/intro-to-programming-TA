# addition_tester2.py

import random
num1 = random.randint(1, 5)
num2 = random.randint(1, 5)

# user_guess = input(f"What is {num1} + {num2}?")
while True:
	user_guess = int(input(f"What is {num1} + {num2}? > "))
	if num1 + num2 == user_guess:
		print("Correct")
		break
	else:
		print("Try again")
	num1 = random.randint(1, 5)
	num2 = random.randint(1, 5)
	# user_guess = input(f"What is {num1} + {num2}? > ")