#candy_betting.py
import random
user_pennies = random.randint(200, 300)
user_candy = 0
while True:
    print(f"You have {user_pennies} pennies and {user_candy} pieces of candy.")
    user_choice = input("Would you like to (bet) with the store or (cash out)? >")
    while user_choice not in ['bet', 'cash out']:
        user_choice = input("Would you like to (bet) with the store or (cash out)? >")
    if user_choice == 'cash out':
        break
    bet_amount = int(input("How many $.25 pieces of candy will you bet? >"))
    if bet_amount * 25 > user_pennies:
        print('Too much!')
        continue
    if random.choice(['win', 'lose']) == 'win':
        print("You won!")
        user_candy += bet_amount
    else:
        print("You lost!")
        user_pennies -= bet_amount * 25
print("Cashing out!")
user_candy += user_pennies // 25
user_pennies = user_pennies % 25
print(f"You ended with {user_candy} pieces of candy and {user_pennies} pennies")
