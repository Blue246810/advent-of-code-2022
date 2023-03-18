# %% [markdown]
# PART 1

# %%
import pandas as pd

# Find width of grid
DATAPATH = "../data/8/data.txt"
grid = pd.read_csv(DATAPATH, header=None)
grid_width = grid.shape[0]

