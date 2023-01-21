# %% [markdown]
# Part 1
#%%
def row_to_score(row):
    def split_string(text):
        middle_index = int(len(text)/2)
        first_half = text[0:middle_index]
        second_half = text[middle_index:]
        return (first_half, second_half)

    both_parts = split_string(row)
    first = both_parts[0]
    second = both_parts[1]

    def common_letters(first, second):
        first_set = set(first)
        second_set = set(second)
        common = first_set.intersection(second_set)
        return common

    letters_in_common = common_letters(first, second)

    def letter_to_number(letter):
        if letter.islower():
            return ord(letter)-96
        if letter.isupper():
            return ord(letter)-38

    number_list = []
    for letter in letters_in_common:
        number = letter_to_number(letter)
        number_list += [number]

    return sum(number_list)

# %%
import pandas as pd
data = pd.read_csv("../data/3/data.txt", names=["input"], sep=" ")
data

#%%
data['score'] = data.apply(lambda row : row_to_score(row["input"]), axis=1)
