import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

input_file = 'data/data_cleaned.csv'
platforms = ['console', 'pc', 'mobile']

def filter_field_value(row1, arg_field, arg_field_val):
    if arg_field == 'type':
        return row1.type == arg_field_val
    elif arg_field == 'group':
        return row1.group == arg_field_val
    return False

def show_plot():
    df = pd.read_csv(input_file)
    arg_platform = sys.argv[1]
    arg_field = sys.argv[2]
    arg_field_val = sys.argv[3]
    if arg_field != 'group' and arg_field != 'type':
        print("Invalid args. Takes field (type, group) as args.")
        return
    
    #print(list(dict.fromkeys(df['type']).keys()))

    platforms_problems = []
    for row in df.iterrows():
        if arg_platform in row[1].platform and filter_field_value(row[1], arg_field, arg_field_val):
            platforms_problems.append(row)
    print(len(platforms_problems))

show_plot()