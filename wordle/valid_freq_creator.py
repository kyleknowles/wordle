import pandas as pd
import numpy as np

df = pd.read_csv('wordle/unigram_freq.csv')
guesses_df = pd.read_csv('wordle/valid_solutions.csv')

word_array = df['word'].to_numpy()
guesses_array = guesses_df['word'].to_numpy()

valid_freq_df = df.merge(guesses_df, how='inner',left_on='word', right_on='word')

valid_freq_df = valid_freq_df[['word']]
valid_freq_df.to_csv('wordle/valid_freq.csv', index=False)
