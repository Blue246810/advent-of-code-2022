#%% [markdown]
# Part 1
#%%
break_position = 0
with open("../data/5/data.txt") as file:
    lines = [line.rstrip() for line in file]
    for position,line in enumerate(lines):
        if line.startswith(" 1 "):
            end_char = int(line[-1])
            break_position = position

#%%
import pandas as pd
data = pd.read_fwf("../data/5/data.txt", widths=[4] * end_char, header=None, nrows=break_position)

