#enough_sleep.py
sleep_amount = input("How much did you sleep last night? >")
sleep_amount = int(sleep_amount)
if sleep_amount <= 5:
    print("You need more sleep")
if sleep_amount >= 10:
    print("Wow you sleep a lot!")
if sleep_amount > 5 and sleep_amount < 10:
    print("You got the right amount!")
