import pandas as pd
import numpy as np

# actually meriam webster
oxford_df = pd.read_csv("wordle/oxford.csv")



oxford_df['Count'] = pd.to_numeric(oxford_df['Count'], errors='coerce')
oxford_df = oxford_df.dropna(subset=['Count'])
oxford_df['Count'] = oxford_df['Count'].astype(int)


oxford_df = oxford_df[oxford_df['Count'] > 2]


oxford_df = oxford_df[["Word"]]

oxford_df = oxford_df.drop_duplicates()


oxford_df['Word'] = oxford_df['Word'].str.lower()

oxford_list = oxford_df.to_numpy()



def parseWords(word):
    word = str(word)
    for letter in word:
        if (ord(letter) < 97) | (ord(letter) > 122):
           
            return False
    return True

oxford_list = [word for word in oxford_list if parseWords(word[0])]
oxford_list = [word for word in oxford_list if len(str(word[0]))> 2]


oxford_df = pd.DataFrame(oxford_list, columns=['word'])

valid_df = pd.read_csv("wordle/all_valid_words.csv")
freq_df = pd.read_csv("wordle/unigram_freq.csv")

oxford_df = oxford_df.merge(valid_df, left_on="word", right_on="word")

freq_df = freq_df[['word']]
oxford_df = oxford_df.merge(freq_df, left_on="word", right_on="word")




oxford_df.to_csv('wordle/oxford_final.csv', index=False)