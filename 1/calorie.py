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

tally.sort(reverse=True)
print(tally)
sum(tally[0:3])
