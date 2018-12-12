import random
import time
from os import system, name


def check(user_input):
    global guess_word
    global display_word
    global life
    index_start = 0
    count = guess_word.count(user_input)
    if user_input == 'quit':
        return
    elif user_input in guess_word and user_input not in display_word:
        for _ in range(count):
            index = guess_word.index(user_input, index_start)
            display_word[index] = user_input
            print(display_word)
            index_start = index + 1
    else:
        print("Invalid Guess")
        life -= 1
    if ''.join(display_word) == guess_word:
        print("Yipee, You won the game!!")
        return


name_list = ['apple', 'banana', 'grapes']
# guess_word=random.choice(name_list)
guess_word = 'banana'
vowels = ['a', 'e', 'i', 'o', 'u']
display_word = []
life = 4
for letter in guess_word:
    if letter in vowels:
        display_word.append(letter)
    else:
        display_word.append('_')
[print(word, end=' ') for word in display_word]
while (life > 0):
    user_input = input()
    user_input.lower()
    check(user_input)
else:
    print("You Loose the game.")
