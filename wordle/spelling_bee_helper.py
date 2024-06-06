import numpy as np
import pandas as pd


spelling_df = pd.read_csv('wordle/all_valid_words.csv')
word_array = spelling_df['word'].to_numpy()

middle_char = str(input("Middle Char: "))
other_chars = str(input("Other Chars: "))

word_array = [word for word in word_array if middle_char in str(word)]

word_array = [word for word in word_array if len(str(word)) > 3]
   


def analyze_word(word_array, index, length):
    for let in word_array[index]:
        if ((let not in (letter for letter in other_chars)) & (let != middle_char)):
            word_array = np.delete(word_array, index)
            length = length - 1
            return [word_array, index, length]
        
    index = index + 1
    return [word_array, index, length]    

initial_length = len(word_array)
total_length = 0
index = 0
length = len(word_array)
while (index < length):
    new_array = analyze_word(word_array, index, length)
    word_array = new_array[0]        
    index = new_array[1]
    length = new_array[2]

    if (total_length % (round(initial_length, -4)/100) == 0):
        print(str(round(total_length/(round(initial_length,-4))*100,1)) + "% Complete")

    total_length = total_length + 1
    


word_array = sorted(word_array, key=len, reverse=True)

old_array = word_array
df = pd.read_csv('wordle/unigram_freq.csv')

valid_array = df['word'].to_numpy()

word_array = [word for word in word_array if word in valid_array]


for word in word_array:
    
    print(word)

next_array = [word for word in old_array if word not in word_array]

for word in next_array:
    print(word)