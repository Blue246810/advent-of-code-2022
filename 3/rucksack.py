# %% [markdown]
# Part 1
#%%    
def letter_to_number(letter: str) -> int:
    if letter.islower():
        return ord(letter)-96
    if letter.isupper():
        return ord(letter)-38
    return 0

#%%
def row_to_score(row: str) -> int:
    def split_string(text: str) -> tuple[str, str]:
        middle_index = int(len(text)/2)
        first_half = text[0:middle_index]
        second_half = text[middle_index:]
        return (first_half, second_half)

    both_parts = split_string(row)

    def common_letters(first: str, second: str) -> set[str]:
        first_set = set(first)
        second_set = set(second)
        common = first_set.intersection(second_set)
        return common

    letters_in_common = common_letters(both_parts[0], both_parts[1])

    number_list = [letter_to_number(letter) for letter in letters_in_common]

    return sum(number_list)

# %%
import pandas as pd
data = pd.read_csv("../data/3/data.txt", names=["input"], sep=" ")
data

#%%
data['score'] = data.apply(lambda row : row_to_score(row["input"]), axis=1)

# %%
data['score'].sum()
# %%
# Part 2
#%%
def common_letters_two(first: str, second: str, third: str) -> set[str]:
    first_set = set(first)
    second_set = set(second)
    third_set = set(third)
    common = first_set.intersection(second_set).intersection(third_set)
    return common

#%%
group: list[str] = []
combined_number_list: list[int] = []
for row in data['input']:
    if len(group) < 3:
        group.append(row)
    else:
        letters_in_common_two = common_letters_two(group[0], group[1], group[2])
        numbers = [letter_to_number(letter) for letter in letters_in_common_two]
        combined_number_list.append(sum(numbers))
        group = []

sum(combined_number_list)

# %%
