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



# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:16:44 2023

@author: Abhay
"""

import pandas as pd

# Read the scraped data from the CSV file
df = pd.read_csv('new_imdb_scraper.csv')

# Define the columns to split
columns_to_split = ['Best Motion Picture of the Year', 'Best Original Screenplay', 'Best Adapted Screenplay',
                    'Best Achievement in Cinematography', 'Best Achievement in Film Editing',
                    'Best Achievement in Production Design', 'Best Achievement in Costume Design',
                    'Best Achievement in Makeup and Hairstyling',
                    'Best Achievement in Music Written for Motion Pictures (Original Score)',
                    'Best Achievement in Music Written for Motion Pictures (Original Song)',
                    'Best Achievement in Visual Effects']

# Create a new DataFrame to store the split values
split_data = []

# Iterate over each row in the original DataFrame
for _, row in df.iterrows():
    # Extract the common columns
    common_data = {key: row[key] for key in df.columns if key not in columns_to_split}
    
    # Split the values in the columns_to_split and create new rows
    for column in columns_to_split:
        values = row[column].split(',')
        for value in values:
            split_row = common_data.copy()
            split_row[column] = value.strip()
            split_data.append(split_row)

# Create the new DataFrame with split values
split_df = pd.DataFrame(split_data)

# Reset the index if needed
split_df = split_df.reset_index(drop=True)

# Display the resulting DataFrame
df.to_csv('dc.csv', index=False)
