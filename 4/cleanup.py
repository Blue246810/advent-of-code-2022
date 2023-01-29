#%% [markdown]
# Part 1

#%%
import pandas as pd
data = pd.read_csv("../data/4/data.txt", names=["sections"], sep=" ")
data = data["sections"].str.split(",", expand=True)
data.columns = ["elf1", "elf2"]

