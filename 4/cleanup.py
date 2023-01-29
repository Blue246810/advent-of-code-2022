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

