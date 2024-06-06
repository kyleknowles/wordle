import numpy as np
import pandas as pd

rf = pd.read_csv('wordle/all_words_rough.csv')
global rough_words_array
rough_words_array = rf['word'].to_numpy()


length = len(rough_words_array)


def analyze_word(index, rough_words_array, length, old_length, error_words):
    if ((str(type(rough_words_array[index])) != "<class 'str'>")):
        error_words.append(str(rough_words_array[index]))
    
    char_list = [ord(char) for char in str(rough_words_array[index])]
    for char in char_list:
        if ((char < 97) | (char > 122)):
           print("Killed: " + rough_words_array[index] + " " + str(index) + " " + str(old_length))
           rough_words_array = np.delete(rough_words_array, index)
           length = length - 1
           return [rough_words_array, index, length, error_words]
        
  
    print("Survived: " + str(rough_words_array[index]) + " " + str(index)+ " " + str(old_length)) 
    index = index + 1 
    return [rough_words_array, index, length, error_words]
    


def analyze_word_list(rough_words_array, length):
    error_words = []
    new_length = length
    index = 0
    while (index < new_length):
        new_array = analyze_word(index, rough_words_array, new_length, length, error_words)
        rough_words_array = new_array[0]
        index = new_array[1]
        new_length = new_array[2]
        error_words = new_array[3]
        length = length + 1
        
    print(error_words)
    return rough_words_array



rough_words_array = analyze_word_list(rough_words_array, length)

final_words_creator_df = pd.DataFrame({"word": rough_words_array})

print(rough_words_array)
final_words_creator_df.to_csv('wordle/all_valid_words.csv', index=False)




