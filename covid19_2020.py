#%%
#1. Setup -mainly importing packages
import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# %%
#2. Extract Dataset
csv_path = 'C:\Users\LENOVO\Desktop\open_ai\Covid19_dlts\cases_malaysia_covid.csv'

# %%
#3. Load the dataset w pandas
df = pd.read_csv(csv_path)