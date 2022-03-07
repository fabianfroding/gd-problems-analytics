import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

input_file = 'data/data_cleaned.csv'

def show_plot():
    df = pd.read_csv(input_file)
    arg_platform = sys.argv[1]
    arg_field = sys.argv[2]
    if (arg_platform != 'pc' and arg_platform != 'console' and arg_platform != 'mobile') or (arg_field != 'group' and arg_field != 'type'):
        print("Invalid args. Takes platform (pc, console, mobile) and field (type, group) as args.")
        return

    field_keys = list(dict.fromkeys(df[arg_field]).keys())
    platform = df[df['platform']==arg_platform]

    vals = []
    for val in field_keys:
        vals.append(len(platform[platform[arg_field] == val]))

    field_header = 'Groups' if arg_field == 'group' else 'Types'
    df_sorted = pd.DataFrame({field_header: field_keys, 'Values': vals}).sort_values("Values", ascending=False)

    #===== Visualization =====#
    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(df_sorted[field_header].values.tolist(), df_sorted['Values'].values.tolist())
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
    
    platform_title = ''
    if arg_platform == 'pc':
        platform_title = 'PC'
    elif arg_platform == 'console':
        platform_title = 'Console'
    else:
        platform_title = 'Mobile'

    ax.set_title('Game development problems for ' + platform_title + ' (by ' + ('Group' if arg_field == 'group' else 'Type') + ')',
                loc ='left', )
    fig.text(0.9, 0.15, '', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)
    
    plt.show()

show_plot()