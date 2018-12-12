import random
import time
import os
def ascii_art():
    global life
    if life==4:
        print("\t\t\t (*)")
    elif life==3:
        print('\t\t\t (*)')
        print('\t\t\t /|\\')
    elif life==2:
        print("\t\t\t (*)")
        print('\t\t\t /|\\')
        print('\t\t\t  |')
    elif life==1:
        print("\t\t\t (*)")
        print('\t\t\t /|\\')
        print('\t\t\t |')
        print('\t\t\t /\\')
    elif life==0:
        print("\t\t\t (*)")
        print('\t\t\t /|\\')
        print('\t\t\t |')
        print('\t\t\t /\\')
        print('DEad')
def check(user_input):
    os.system('cls')
    print("WELCOME TO HANGMAN GAME\n\tType QUIT to EXIT from game.\n\tYou have Three chances.\n\tThe WORD is name of FRUIT")

    global life
    index_start = 0
    count = guess_word.count(user_input)
    if user_input == 'quit': #exits the program if user enters quit
        return True
    elif user_input=='':
        print("Invalid Guess!!\nLife Left: ",life)
        life-=1
    elif user_input in guess_word and user_input not in display_word: #checks if letter is in the original word
        for _ in range(count):
            index = guess_word.index(user_input, index_start)
            display_word[index] = user_input #inserts the letter at its position
            print(display_word)
            index_start = index + 1
    else:
        print("Invalid Guess!!\nLife Left: ", life)
        life -= 1
    if ''.join(display_word) == guess_word: #check if the length of both original and guessed string is equal or not
        print("Yipee, You won the game!!")
        return True

f=open("words.txt",'r') #opens a file
name_list = f.read().splitlines()
guess_word=random.choice(name_list)
#vowels = ['a', 'e', 'i', 'o', 'u'] #initialize list of vowels
print("WELCOME TO HANGMAN GAME\n\tType QUIT to EXIT from game.\n\tYou have Three chances.\n\tThe WORD is name of FRUIT")
display_word = []
life = 5
[display_word.append('_') for letter in guess_word] #creates a list with vowels and _ at consonant position
#[print(word, end=' ') for word in display_word] #print the word
while (life > 0): #check the life, should be greater than 0
    ascii_art()
    [print(word, end=' ') for word in display_word]
    user_input = input()
    user_input=user_input.lower() #converts user input in lower case
    flag=check(user_input) #class a function which check and append the letter
    if flag:
        break
else:
    ascii_art()
    print("You Loose the game.")
