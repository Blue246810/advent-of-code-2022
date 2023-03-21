# %% [markdown]
# PART 1

# %%
# read input
with open("../data/9/data.txt") as file:
    lines = [line.rstrip() for line in file]

# %%
# create variables for movement of head, tail and tail positions has been in
head: tuple = (0,0)
tail: tuple = (0,0)
tail_pos: list = []
allowable_distance = 1

#%%
# where head moves to 
for row in lines:
    direction = row.split(" ")[0]
    steps = int(row.split(" ")[1])

    for _ in range(steps):
        if direction == "R":
            head = (head[0]+1, head[1])
        elif direction == "L":
            head = (head[0]-1, head[1])
        elif direction == "U":
            head = (head[0], head[1]+1)
        else:
            head = (head[0], head[1]-1)

