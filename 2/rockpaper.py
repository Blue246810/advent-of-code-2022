# %% [markdown]
# Part 1
# %% [markdown]
# A/X - Rock - 1
# B/Y - Paper - 2
# C/Z - Scissors - 3
# 
# Lost - 1
# Draw - 3
# Won - 6

# %%
import pandas as pd
plan = pd.read_csv("../data/2/data.txt", names=["theirs", "ours"], sep=" ")

# %%
def map_letter_to_score(letter):
    if letter == 'X':
        return 1
    elif letter == 'Y':
        return 2
    elif letter == 'Z':
        return 3

def game_score(theirs, ours):
    if theirs == 'A' and ours == 'X':
        return 3
    elif theirs == 'A' and ours == 'Y':
        return 6
    elif theirs == 'A' and ours == 'Z':
        return 0
    elif theirs == 'B' and ours == 'X':
        return 0
    elif theirs == 'B' and ours == 'Y':
        return 3
    elif theirs == 'B' and ours == 'Z':
        return 6
    elif theirs == 'C' and ours == 'X':
        return 6
    elif theirs == 'C' and ours == 'Y':
        return 0
    elif theirs == 'C' and ours == 'Z':
        return 3

plan['strategy_score'] = plan.apply(lambda row : map_letter_to_score(row['ours']) , axis=1)
plan['game_score'] = plan.apply(lambda row : game_score(row['theirs'], row['ours']), axis=1)
plan['round_score'] = plan['strategy_score'] + plan['game_score']


# %%
plan.sum()

