# %% [markdown]
# Part 1
# %%
test = "abba"

def split_string(text):
    middle_index = int(len(text)/2)
    first_half = text[0:middle_index]
    second_half = text[middle_index:]
    return (first_half, second_half)

split_string(test)

