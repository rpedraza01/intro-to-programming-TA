#make_change.py
import random
user_pennies = int(input("How many pennies do you have? > "))
quarters = user_pennies // 25
user_pennies = user_pennies % 25
print(f"You have {quarters} quarters")
dimes = user_pennies // 10
user_pennies = user_pennies % 10
print(f"You have {dimes} dimes")
nickles = user_pennies // 5
user_pennies = user_pennies % 5
print(f"You have {nickles} nickles")
print(f"You have {user_pennies} pennies remaining")
