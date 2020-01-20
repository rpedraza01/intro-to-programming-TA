#rock_paper_scissors.py
while True:
    import random
    choice_list = ['rock', 'paper', 'scissors']
    user_choice = input(f"{choice_list[0]}, {choice_list[1]}, {choice_list[2]}! Shoot! ")
    computer_choice = random.choice(choice_list)
    print(f"{computer_choice.title()}")
    if computer_choice == 'rock':
        if user_choice == 'rock':
            print("Tie!")
        elif user_choice == 'paper':
            print("You win!")
        elif user_choice == 'scissors':
            print("You lose!")
    if computer_choice == 'paper':
        if user_choice == 'rock':
            print("You lose!")
        elif user_choice == 'paper':
            print("Tie!")
        elif user_choice == 'scissors':
            print("You win!")
    if computer_choice == 'scissors':
        if user_choice == 'rock':
            print("You win!")
        elif user_choice == 'paper':
            print("You lose!")
        elif user_choice == 'scissors':
            print("Tie!")
    exit_string = input("Best two out of three? ")
    if exit_string != 'yes':
        break
