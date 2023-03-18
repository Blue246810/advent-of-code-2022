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

