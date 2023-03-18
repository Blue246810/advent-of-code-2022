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

# %% [markdown]
# PART 2

# %%
# Create function to find number of trees between entry and tree >= entry
def distance_entry_to_tree(direction, entry):
    number_of_trees = 0
    for tree in direction:
        if tree < entry:
            number_of_trees += 1
        elif tree == entry:
            number_of_trees += 1
            break
        else:
            break
    return number_of_trees

tree_list = []
for row_number, row in trees.iterrows():
 
    for col_number, entry in enumerate(row): 
        above = trees[0: row_number][col_number][::-1]
        below = trees[row_number+1: ][col_number]
        left = trees.iloc[row_number][0: col_number][::-1]
        right = trees.iloc[row_number][col_number+1: ]

        above_no = distance_entry_to_tree(above, entry)
        below_no = distance_entry_to_tree(below, entry)
        left_no = distance_entry_to_tree(left, entry)
        right_no = distance_entry_to_tree(right, entry)
        total = above_no * below_no * left_no * right_no
        tree_list += [total]

max(tree_list)
