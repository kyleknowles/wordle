
import pandas as pd
import numpy as np

df = pd.read_csv('wordle/valid_freq.csv')
five_letter_array = df['word'].to_numpy()


def wordle_solver(five_letter_array):
    print("Welcome to Wordle Helper")
    for guess in range(5):
        word = input("Choose a word: ").lower()
        while (len(word) != 5):
            print("Word must be of length 5")
            word = input("Choose a word: ").lower()

        word_data = input("And what information did that give you?: ").upper()
        while (len(word_data) != 5):
            print("Information must be of length 5")
            word_data = input("And what information did that give you?: ").upper()

        # If you win
        if (word_data == "GGGGG"):
            print("Congratulations, you got it!!")
            return(0)
        
        for data_letter in range(5):
            ## Have to add cases where there are two of the same letter
            
            if (word_data[data_letter] == "B"):
                guess_count = 0
                for letter in range(5):
                    if ((word_data[letter] == "G") | (word_data[letter] == "Y")) & (word[data_letter] == word[letter]):
                        guess_count += 1

    
                five_letter_array = [five_word for five_word in five_letter_array if word[data_letter] != five_word[data_letter]]
                five_letter_array = [five_word for five_word in five_letter_array if five_word.count(word[data_letter]) == guess_count]
               

            elif (word_data[data_letter] == "G"):
                five_letter_array = [five_word for five_word in five_letter_array if word[data_letter] == five_word[data_letter]]
                
            elif (word_data[data_letter] == "Y"):

                five_letter_array = [five_word for five_word in five_letter_array if ((word[data_letter] in five_word) & (word[data_letter] != five_word[data_letter]))]
                
                
        print("Possible Words:")
        word_length = 20
        if (len(five_letter_array) < 20):
            word_length = len(five_letter_array)
            
        for common_word in range (word_length):
            print(str(common_word+1) + ". " + five_letter_array[common_word])
        print()
                        



   
wordle_solver(five_letter_array)

