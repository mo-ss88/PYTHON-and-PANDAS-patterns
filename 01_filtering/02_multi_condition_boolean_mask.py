# you can make a multiline string by using three quotes before and after the multi line string it 
# it creates a string that can span multiple lines ( """..."""(or ''' ... ''') 
"""
Pattern: df[condition with &, |, ~]
Goal: filter rows using multiple conditions in pandas.

Think of it as:
df_filtered = df[
    (df['col1'] compare_op value1)
    LOGICAL_OP
    (df['col2'] compare_op value2)
]
"""

# Notes:
# - Three quotes (""" or ''') create a multi-line string.
# - Here we use it like a big comment at the top (a docstring).
# - Python sees this string but we don't store it in a variable,
#   so it just gets ignored when the program runs.

import pandas as pd

# Load data (TripleTen path, adjust if needed)
df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# Example 1 – non-sports Wii games
df_wii_nonsports = df[
    (df['platform'] == 'Wii') &
    ~(df['genre'] == 'Sports')
]

print(df_wii_nonsports.head())
