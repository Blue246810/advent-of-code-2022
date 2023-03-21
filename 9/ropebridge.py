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

