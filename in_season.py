#in_season.py
import random
ingredient_list = ['carrots', 'kiwis']
food_list = ['carrot cake', 'kiwi cake']
chosen_food = input(f"Do you want to have {food_list[0]} or {food_list[1]}?")
while chosen_food not in food_list:
    chosen_food = input(f"Do you want to have {food_list[0]} or {food_list[1]}?")
in_season = random.choice(ingredient_list)
print(f"{in_season.title()}s are in season.")
if in_season == 'carrots':
    if chosen_food == 'carrot cake':
        print("You can have carrot cake!")
    if chosen_food == 'kiwi cake':
        print("Oh no, carrots are in season!")
if in_season == 'kiwis':
    if chosen_food == 'carrot cake':
        print("You're outta luck")
    #if chosen_food == 'kiwi cake':
    #elif chosen_food == 'kiwi cake':
else:
    
    if chosen_food == 'kiwi cake':
        print("Eat some kiwi cake!")
