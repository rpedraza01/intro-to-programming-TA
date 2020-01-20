#password_generator.py
while True:
    print("Want to make a new password?")
    import random
    import string
    chosen_length =  input("Choose password length >")
    out_string = ''
    for count in range(0, int(chosen_length)):
        out_string = out_string + random.choice(string.digits + string.punctuation + string.ascii_letters)
    print(out_string)
    exit_string = input("Want another password? ")
    if exit_string != 'yes':
        break
