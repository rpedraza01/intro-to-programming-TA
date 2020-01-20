    #magic_eight_ball.py
while True:
    print("Welcome to The Magic Eight Ball!")
    import random
    answers_list = ['Yes, absolutely', 'NEVER!', 'Sure, why the heck not?', 'Fuggedaboutit!', 'Error']
    user_question = input('Magic eight ball...? ')
    computer_answer = random.choice(answers_list)
    print(f"{computer_answer.title()}")
    exit_string = input("Ask another question? ")
    if exit_string != 'yes':
        break
