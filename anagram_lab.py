#anagram_lab.py
import os
first_word = input("What is your first word? > ")
second_word = input("What is your second word? > ")
first_word = first_word.lower()
second_word = second_word.lower()
first_word = first_word.replace(' ', '')
second_word = second_word.replace(' ', '')
first_list = list(first_word)
second_list = list(second_word)
first_list.sort()
second_list.sort()
if first_list == second_list:
    print("You got an anagram!")
else:
    print("That is not an anagram!")
