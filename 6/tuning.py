#%% [markdown]
# PART 1

#%%
with open("../data/6/data.txt", 'r') as file:
    datastream = file.read()

datastream

#%% 
for index in range(len(datastream)):
    four_chars = datastream[index: index+14]
    has_duplicates = len(set(four_chars)) != len(four_chars)
    if not has_duplicates:
        print(index+14)
        break
