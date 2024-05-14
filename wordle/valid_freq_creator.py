import pandas as pd
import numpy as np

df = pd.read_csv('wordle/unigram_freq.csv')
guesses_df = pd.read_csv('wordle/valid_solutions.csv')

word_array = df['word'].to_numpy()
guesses_array = guesses_df['word'].to_numpy()

valid_freq_df = df.merge(guesses_df, how='inner',on='word')

# array of valid words that need to be added to df 
lost_words = [word for word in guesses_array if word not in word_array]
lost_words_df = pd.DataFrame({"word": lost_words})
valid_freq_df = pd.concat([valid_freq_df, lost_words_df], ignore_index=True)

valid_freq_df = valid_freq_df[['word']]
valid_freq_df.to_csv('wordle/valid_freq.csv', index=False)
