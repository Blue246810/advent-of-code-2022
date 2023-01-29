#%% [markdown]
# Part 1

#%%
import pandas as pd
data = pd.read_csv("../data/4/data.txt", names=["sections"], sep=" ")
data = data["sections"].str.split(",", expand=True)
data.columns = ["elf1", "elf2"]

#%%
def splitcol(column_name, name):
    data = column_name.str.split("-", expand=True)
    data.columns = [name + "low", name + "high"]
    data[name + "low"] = data[name + "low"].astype(int)
    data[name + "high"] = data[name + "high"].astype(int)
    return data

#%%
data_elf1 = splitcol(data["elf1"], "elf1")
data_elf2 = splitcol(data["elf2"], "elf2")
data_combined = pd.concat([data_elf1,data_elf2], axis=1)

#%%
def range_contained(low1, high1, low2, high2):
    if high2 <= high1 and low2 >= low1: 
        return 1
    elif high1 <= high2 and low1 >= low2:
        return 1
    else:
        0

#%%
data_combined['range_contained'] = data_combined.apply(lambda row : range_contained(row["elf1low"], row["elf1high"], row["elf2low"], row["elf2high"]), axis=1)

# %%
data_combined['range_contained'].count()

#%% [markdown]
# Part 2

#%%
def range_contained_two(low1, high1, low2, high2):
    if high2 <= high1 and low2 >= low1: 
        return 1
    elif high1 <= high2 and low1 >= low2:
        return 1
    elif low2 >= low1 and low2 <= high1:
        return 1
    elif low1 >= low2 and low1 <= high2:
        return 1
    else:
        0

