import os
import numpy as np
import pandas as pd
import csv
import sys
import scipy.stats as stats

input_file = 'data/data_cleaned.csv'
output_file = 'data/data_genre_categorical.csv'

def format_csv(file):
    raw_data = pd.read_csv(file)

    genre = sys.argv[1]
    problem_type = sys.argv[2]
    
    genre_ids = []

    for val in raw_data['genre']:
        if val == genre:
            genre_ids.append(1)
        else:
            genre_ids.append(2)

    print(genre_ids)

    problem_ids = []

    for val in raw_data['type']:
        if val == problem_type:
            problem_ids.append(1)
        else:
            problem_ids.append(2)

    print(problem_ids)

    #create 2x2 table
    data = np.array([genre_ids, problem_ids])

    #Chi-squared test statistic, sample size, and minimum of rows and columns
    X2 = stats.chi2_contingency(data, correction=False)[0]
    n = np.sum(data)
    minDim = min(data.shape)-1

    #calculate Cramer's V 
    V = np.sqrt((X2/n) / minDim)

    #display Cramer's V
    print(V)


    #for val in raw_data.values:
    #    print(val)

    '''#========== Get fields ==========#
    platforms = raw_data['platform'].values.tolist()
    genres = raw_data['genre'].values.tolist()
    modes = raw_data['mode'].values.tolist()
    groups = raw_data['group'].values.tolist()
    types = raw_data['type'].values.tolist()

    formatted_combined = [platforms, genres, modes, groups, types]
    formatted_transposed = np.transpose(formatted_combined)

    #========== Write new formatted csv file ==========#
    f = open(output_file, 'w', newline='')
    writer = csv.writer(f)

    # Write header
    writer.writerow(['platform', 'genre', 'mode', 'group', 'type'])

    # Write rows
    for vals in formatted_transposed:
        writer.writerow(vals)

    f.close()'''

format_csv(input_file)
