import os
import numpy as np
import pandas as pd
import csv
import sys
import scipy.stats as stats

input_file = 'data/data_cleaned.csv'

def format_csv(file):
    raw_data = pd.read_csv(file)

    platform = sys.argv[1]
    problem_type = sys.argv[2]
    
    platform_ids = []

    for val in raw_data['platform']:
        if val == platform:
            platform_ids.append(1)
        else:
            platform_ids.append(2)

    print(platform_ids)

    problem_ids = []

    for val in raw_data['type']:
        if val == problem_type:
            problem_ids.append(1)
        else:
            problem_ids.append(2)

    print(problem_ids)

    #create 2x2 table
    data = np.array([platform_ids, problem_ids])

    #Chi-squared test statistic, sample size, and minimum of rows and columns
    X2 = stats.chi2_contingency(data, correction=False)[0]
    n = np.sum(data)
    minDim = min(data.shape)-1

    #calculate Cramer's V 
    V = np.sqrt((X2/n) / minDim)

    #display Cramer's V
    print(V)

format_csv(input_file)
