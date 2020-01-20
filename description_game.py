#description_game.py
import os
chosen_word = input("What word did the users agree on? > ")
assoc_num = input("How many associating words will the players say? > ")
assoc_num = int(assoc_num)
player1_words = []
player2_words = []
for player in [player1_words, player2_words]:
    while len(player) < assoc_num:
        user_word = input("Give me an associating word > ")
        player.append(user_word.lower())
    os.system('clear')
player1_words.sort()
player2_words.sort()
if player1_words == player2_words:
    print("You win!")
else:
    print("You lose!")
