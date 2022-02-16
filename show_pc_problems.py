import os
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

input_file = 'data/data_cleaned.csv'

def show_pc_problem_types(file):
    df = pd.read_csv(file)

    problem_types = list(dict.fromkeys(df['type']).keys())

    pc = df[df['platform']=='pc']

    problem_types_vals = []
    for problem_type in problem_types:
        problem_types_vals.append(len(pc[pc['type'] == problem_type]))

    df_sorted = pd.DataFrame({'Types': problem_types, 'Values': problem_types_vals}).sort_values("Values", ascending=False)

    #===== Visualization =====#
    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(df_sorted['Types'].values.tolist(), df_sorted['Values'].values.tolist())
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)
    
    ax.invert_yaxis()
    
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight ='bold',
                color ='grey')
    
    ax.set_title('Game development problems for PC',
                loc ='left', )
    fig.text(0.9, 0.15, '', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)
    
    plt.show()

show_pc_problem_types(input_file)