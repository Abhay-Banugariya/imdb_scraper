# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:43:03 2023

@author: Abhay
"""

import pandas as pd

df = pd.read_csv('imdb_scraper.csv')
df.columns
df_exploded = df.explode('Best Motion Picture of the Year')
print(df_exploded)
# transpose the source df
tdf = df_exploded.T
# # df['column_to_replace'] = df['column_to_replace'].replace('old_value', 'new_value')

# #made first row as a header of column
# tdf = tdf.set_axis(tdf.iloc[0], axis=1)

# #parsing movie name


# The 'csv_column' will now contain a list of values for each row

#transposing into 4xn tabular. Year, movie name, category, status:won or nominated 
