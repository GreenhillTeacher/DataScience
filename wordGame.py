# input, random, time to delay
import random
import time
from urllib.request import urlopen
import json
import random
name = input("What is your name? ")

#JSON Fetcher

def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        print('here')
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word
if __name__ == "__main__":
    request = urlopen("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json")
    response = request.read()
    data = json.loads(response)
    print(name, end = '')
    game = input(",do you want to play? ")
    while game.lower() == 'yes':
        difficulty = input("Easy, Medium, or Hard? (1,2,3)")
        word = ''
        if difficulty == '1':
            print("Easy Mode")
            word  = word_prompt(data, 5)
        elif difficulty == '2':
            print("Medium Mode")
            word = word_prompt(data, 7)
        elif difficulty == '3':
            print("Hard Mode")
            word = word_prompt(data,10)
        else:
            print("error, running in easy")
        print(word)
        #Level checker
        guess=''
        uniqueChar = set(word)
        turns= len(uniqueChar) +5
        print (name, " ,you have " + str(turns) + " turns to guess the word", end='')
        print()
        win = False

        while turns>0 and win== False:
            win = True
            for char in word:
                if char in guess:
                     print(char, end=' ')
                else: 
                    print('_', end=' ')
                    win = False
            print()
            print(name, end=' ')
            letter= input(" please give me a letter : ")
            guess +=letter
            turns -=1
            #Guess is out of order, so instead write a string with the charecter added to check, 
            #check if underscore
        if win == True:
            print("you win yay! The word was " + word)
        else:
            print("loser. The word was " + word)
        game=input(" Do you want to play again ")
    print(name, ", come back anytime!")
    time.sleep(5)
# Need to add winning statement
#Need wordlist w/difficulty
#bug w/ wrong char to correct answer, rewrite winpoints