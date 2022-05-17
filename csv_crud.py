"""
CSV comma separated value

file format for importing and exporting big datasets,
The reason why csv file is preferred over an Excel file is that csv files consumes less memory than Excel.

"""

# Writing a csv file?

import csv
import pandas as pd
data ={"Name": ["sree", "dhath", "kris", "dhanil"], "Age": [12,16,18,20]}
data = pd.DataFrame(data)
data.to_csv("age_data.csv", index=False)
print(data.head())

# read csv file

data = pd.read_csv("age_data.csv")
print(data.head())