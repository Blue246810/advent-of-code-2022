# %% [markdown]
# PART 1

# %%
import pandas as pd

# Find width of grid
DATAPATH = "../data/8/data.txt"
grid = pd.read_csv(DATAPATH, header=None)
grid_width = grid.shape[0]

# %%
# Read file into columns and rows
trees = pd.read_fwf(DATAPATH, widths=[1] * grid_width, header=None)

# %%
# Calc edge of the tree grid
grid_edge = (trees.shape[0]-1) * (trees.shape[1]-1)

# %%
# Find trees visible from outside
import math 

counter = 0
inside_vis = []
for row_number, row in trees.iterrows():
    # print(row_number, row)
    for col_number, entry in enumerate(row): 
        # print(row_number, col_number)
        above = trees[0: row_number][col_number]
        max_above = above.max()
        below = trees[row_number+1: ][col_number]
        max_below = below.max()
        left = trees.iloc[row_number][0: col_number]
        max_left = left.max()
        right = trees.iloc[row_number][col_number+1: ]
        max_right = right.max()

        if math.isnan(max_above) or math.isnan(max_below) or math.isnan(max_left) or math.isnan(max_right):
            counter += 1
            continue

        if entry > max_above or entry > max_below or entry > max_left or entry > max_right:
            counter += 1
counter

