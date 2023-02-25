#%% [markdown]
# Part 1

#%%
DATA_PATH = "../data/5/data.txt"
#%%
break_position = 0
with open(DATA_PATH) as file:
    lines = [line.rstrip() for line in file]
    for position,line in enumerate(lines):
        if line.startswith(" 1 "):
            end_char = int(line[-1])
            break_position = position

#%%
import pandas as pd
data = pd.read_fwf(DATA_PATH, widths=[4] * end_char, header=None, nrows=break_position)

#%%
col_list: list[list[str]] = []
for _,col in data.iteritems():
    non_na_series = col.dropna()
    non_na_list = non_na_series.to_list()
    non_na_list.reverse()
    col_list += [non_na_list]

#%%
data_beyond_break = pd.read_csv(DATA_PATH, header=None, skiprows=break_position+1, sep=" ")
#%%
blocks_to_move = data_beyond_break[1]
start_pos = data_beyond_break[3]
end_pos = data_beyond_break[5]

#%%
import copy
working_col_list = copy.copy(col_list)
for i in range(len(blocks_to_move)):
    how_many_to_move = blocks_to_move[i]
    from_where = start_pos[i]-1
    to_where = end_pos[i]-1
    from_list = working_col_list[from_where]
    to_list = working_col_list[to_where]
    new_additions = from_list[-how_many_to_move:]
    # new_additions.reverse() PART 1
    from_list = from_list[0:len(from_list)-how_many_to_move]
    to_list = to_list + new_additions
    
    working_col_list[from_where] = from_list
    working_col_list[to_where] = to_list

comb = []
for bucket in working_col_list:
    comb += bucket[-1:]
test = ''.join(str(element) for element in comb)
print(''.join(letter for letter in test if letter.isalpha()))