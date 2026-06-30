import pandas as pd
import numpy as np


df = pd.read_csv("wordle/avcsv")

word_array = df['word'].to_numpy()
#other_array = other_df['word'].to_numpy()

side1 = input("Side 1: ")
side2 = input("Side 2: ")
side3 = input("Side 3: ")
side4 = input("Side 4: ")

allsides = side1 + side2 + side3 + side4
not1 = side2 + side3 + side4
not2 = side1 + side3 + side4
not3 = side1 + side2 + side4
not4 = side1 + side2 + side3


letters_left = allsides
new_word = ""

def valid_word(word):
    valid_letters = allsides
    for letter in word:
        if (letter not in valid_letters):
            return False
        elif (letter in side1):
            valid_letters = not1
        elif (letter in side2):
            valid_letters = not2
        elif (letter in side3):
            valid_letters = not3
        elif (letter in side4):
            valid_letters = not4
    return True



word_array = [word for word in word_array if len(str(word)) > 2]
word_list = [word for word in word_array if valid_word(str(word))]

def printWordList(wordlist):
    for word in range (len(wordlist) - 1):
        print(wordlist[word], end=" -> ")

    print(wordlist[-1])


def unique_letters(word):
    return(len(set(word) - set(new_word)))




print()


new_list = word_list
wordlist = []
wordCount = 0

new_list.sort(key=unique_letters, reverse=True)

total_word_list = []

def findList(letters_left, new_word, word_list, wordlist):
       word_count = 0
       while (len(letters_left) > 0):
            word_count = word_count + 1

            last_letter = new_word[-1]
            new_list = [word for word in word_list if word[0] == last_letter]

            new_list.sort(key=unique_letters, reverse=True)
            
            if (len(new_list) == 0):
                return wordlist

            
            
            new_word = new_word + new_list[0]

            wordlist.append(new_list[0])
            letters_left = str(set(letters_left) - set(new_word)).replace(" ","").replace("'","").replace(",","").replace("{","").replace("}","").replace("set()","")
            if (word_count > 5):
                return (wordlist)

       total_word_list.append(wordlist)
       return (wordlist)

for word in new_list:

    wordlist = []
    new_word = new_word + word

    wordlist.append(word)

    wordlist = findList(letters_left, new_word, word_list, wordlist)
    
    new_list = word_list
    wordlist = []
    letters_left = allsides
    new_word = ""


# print all paths in order of size
total_word_list = sorted(total_word_list, key=len)
for list in total_word_list:
    printWordList(list)

