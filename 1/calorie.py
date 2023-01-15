# %% [markdown]
# Part 1

# %%
with open("data.txt") as file:
    lines = file.readlines()

tally = []
count = 0
for line in lines:
    if line.isspace():
        tally += [count]
        count = 0
        continue
    else:  
       line = int(line)    
       count += line

print(max(tally))

# %% [markdown]
# Part 2
# %%
# Another way to achieve part 2 using numpy
import numpy as np
numpytally = np.asarray(tally)
numpytally[0:3].sum()
