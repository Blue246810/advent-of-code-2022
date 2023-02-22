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

#%%
col_list: list[list[str]] = []
for _,col in data.iteritems():
    non_na_series = col.dropna()
    non_na_list = non_na_series.to_list()
    non_na_list.reverse()
    col_list += [non_na_list]

#%%
data_beyond_break = pd.read_csv("../data/5/data.txt", header=None, skiprows=break_position+1, sep=" ")

#%%
blocks_to_move = data_beyond_break[1]
start_pos = data_beyond_break[3]
end_pos = data_beyond_break[5]

