import os
import numpy as np
import pandas as pd
import csv
from datetime import datetime

input_file = 'data/data_raw.csv'
output_file = 'data/data_cleaned.csv'

def format_csv(file):
    raw_data = pd.read_csv(file)

    #========== Get fields ==========#
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

    f.close()

format_csv(input_file)
