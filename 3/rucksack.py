# %% [markdown]
# Part 1
# %%
test = "abccde"

def split_string(text):
    middle_index = int(len(text)/2)
    first_half = text[0:middle_index]
    second_half = text[middle_index:]
    return (first_half, second_half)

both_parts = split_string(test)
first = both_parts[0]
second = both_parts[1]
#%%
def common_letters(first, second):
    first_set = set(first)
    second_set = set(second)
    common = first_set.intersection(second_set)
    return common
# %%
common_letters(first, second)
#%%
def letter_to_number(letter):
    if letter.islower():
        return ord(letter)-96
    if letter.isupper():
        return ord(letter)-38

