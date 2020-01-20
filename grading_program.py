#grading_program.py
grade_amount = input("What is your grade?")
grade_amount = int(grade_amount)
if grade_amount >= 90:
    print("You get an A, you will succeed in life!")
if grade_amount >= 80 and grade_amount <= 89:
    print("You get a B!")
if grade_amount >= 70 and grade_amount <= 79:
    print("You get a C!")
if grade_amount >= 60 and grade_amount <= 69:
    print("You get a D!")
if grade_amount <= 59:
    print("You fail!")
