import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import glob

# import os
# for dirname, _, filenames in os.walk('input'):
#     for filename in filenames:
#         os.path.join(dirname, filename)

path = r'C:\Users\Trevor\Documents\NCAABasketball\input'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

print(df.head())
print(df.tail())