#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = "rasFile.ras"


# Open file and read into a list
file_object = open(file_name)
lines = file_object.readlines()
lines_array = np.array(lines)

# Filter out non-numerical data 
mask = np.char.find(lines, '*') == -1
start_index = np.argmax(mask) if np.any(mask) else None
mask = mask[start_index:]
lines = lines[start_index:]
end_index = np.argmax(~mask) if np.any(~mask) else None
if end_index:
    lines = lines[:end_index]

# Separate each row and datapoint
data_rows = [line.strip().split() for line in lines]

# Insert data into a dataframe, format and save 
raw_dataframe = pd.DataFrame(data_rows, columns = ["2_theta", "intensity", "unk"])
raw_dataframe = raw_dataframe.astype({'2_theta': 'float64', 'intensity': 'float64', 'unk': 'float64'})
raw_dataframe.to_csv('raw_output.csv', index=False)

# Create visualization plot for raw data
plt.plot(raw_dataframe['2_theta'], raw_dataframe['intensity'])
plt.xlabel('2_theta')
plt.ylabel('intensity')
plt.title('Line Plot of 2_theta vs intensity')
plt.grid(True)
plt.savefig("raw_plot.png", dpi=300, bbox_inches='tight', transparent=True)

# Create a copy of original dataframe
processed_dataframe = raw_dataframe.copy()

# Change x-axis to start at 0
processed_dataframe["2_theta"] = processed_dataframe["2_theta"] - np.min(processed_dataframe["2_theta"])
processed_dataframe.to_csv('processed_output.csv', index=False)

# Create visualization plot for processed data
plt.plot(processed_dataframe['2_theta'], processed_dataframe['intensity'])
plt.xlabel('2_theta')
plt.ylabel('intensity')
plt.title('Line Plot of 2_theta vs intensity')
plt.grid(True)
plt.savefig("processed_plot.png", dpi=300, bbox_inches='tight', transparent=True)