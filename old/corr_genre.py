import os
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
import seaborn as sns

input_file = 'data/data_cleaned.csv'

def show_plot():
    df = pd.read_csv(input_file)

    types = df['type'].values.tolist()
    genres = df['genre'].values.tolist()

    # assign data of lists.
    data = {'Type': types, 'Genre': genres}
    # Create DataFrame.
    df = pd.DataFrame(data)
    # Print the output.
    print(df)

    corr = df['Type'].corr(df['Genre'])
    print(corr)

    '''mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    ax = sns.heatmap(
        corr, 
        vmin=None, vmax=None, center=0,
        cmap=sns.diverging_palette(255, 0, as_cmap=True),
        square=True,
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=35,
        horizontalalignment='right'
    )
    ax.set_yticklabels(
        ax.get_yticklabels(),
        rotation=0
    )
    ax.set_title("Influences on funding")
    plt.show()'''

show_plot()