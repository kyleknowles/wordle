import numpy as np
import pandas as pd


spelling_df = pd.read_csv('wordle/all_valid_words.csv')
word_array = spelling_df['word'].to_numpy()

middle_char = str(input("Middle Char: "))
other_chars = str(input("Other Chars: "))
print("Starting Length: " + str(len(word_array)))
word_array = [word for word in word_array if middle_char in str(word)]
print("After Middle Length: " + str(len(word_array)))
word_array = [word for word in word_array if len(str(word)) > 3]
   
print("After Small Words Length: " + str(len(word_array)))

def anal_word(word, other_chars):
    for i in range(len(word)):
        let = str(word[i])
        if ((let not in (letter for letter in other_chars)) & (let != middle_char)):
            return False
    return True

word_array = [word for word in word_array if (anal_word(str(word), other_chars))]

print("Valid Words Length: " + str(len(word_array)))


word_array = sorted(word_array, key=len, reverse=True)

old_array = word_array
df = pd.read_csv('wordle/unigram_freq.csv')

valid_array = df['word'].to_numpy()


word_array = [word for word in word_array if word in valid_array]

bad_array = []

for word in word_array:
    result = df[df['word'] == word]
    value = int(result['count'].values[0])
    if (value < 0):
        bad_array.append(word + ", " + str(value))
    else:
        print(str(word) + ", " + str(value))

worst_array = [word for word in old_array if word not in word_array]

print()
print("Possibly:")
for word in bad_array:
    print(word)

print()
print("Probably Not:")
for word in worst_array:
    print(word)