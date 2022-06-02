# pyscript.write('print', "Let's compute π:")
#
#
# def compute_pi(n):
#   pi = 2
#   for i in range(1, n):
#     pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
#   return pi
#
#
# pi = compute_pi(100000)
# s = f"π is approximately {pi:.3f}"
# pyscript.write('print1', s)
#
# print('This is using the print() function')


import pandas as pd
# import re
import matplotlib.pyplot as plt

to_drop = ['id', 'created', 'modified', 'product_code', 'id_x', 'created_x', 'modified_x', 'category_id',
           'id_y', 'created_y', 'modified_y']

df = pd.read_csv('loblaws-mintel_upc_duplicates.csv').drop(columns=to_drop)
mintel = df.loc[df['store'] == 'MINTEL'].sort_values(by='upc_code').reset_index(drop=True)
loblaws = df.loc[df['store'] == 'LOBLAWS'].sort_values(by='upc_code').reset_index(drop=True)


cols_to_match = ['serving_size_raw', 'name', 'calories', 'saturatedfat', 'sodium']

row_list = []
for i, r in mintel.iterrows():
  new_row = []
  for c in cols_to_match:
    new_row.append(r[c])
    new_row.append(loblaws.iloc[i][c])
    new_row.append(r[c] == loblaws.iloc[i][c])

  row_list.append(new_row)

columns = []
for c in cols_to_match:
  columns.append(f'{c}_mintel')
  columns.append(f'{c}_loblaws')
  columns.append(f'{c}_exact_match')

match_df = pd.DataFrame(row_list, columns=columns)
match_df['upc_code'] = mintel['upc_code']
match_df['total_match_count'] = match_df.loc[:, match_df.columns.str.contains('exact_match')].sum(axis=1)

x = match_df.head(3)
# pyscript.write('table', x)


calories_match = len(match_df[match_df['calories_exact_match'] == True])
calories_nomatch = len(match_df[match_df['calories_exact_match'] == False])
# print('calories', calories_match, calories_nomatch)
pyscript.write('cal-match', calories_match)
pyscript.write('cal-noM', calories_nomatch)

satfat_match = len(match_df[match_df['saturatedfat_exact_match'] == True])
satfat_nomatch = len(match_df[match_df['saturatedfat_exact_match'] == False])
# print('satfat', satfat_match, satfat_nomatch)

sodium_match  = len(match_df[match_df['sodium_exact_match'] == True])
sodium_nomatch = len(match_df[match_df['sodium_exact_match'] == False])
# print('sodium', sodium_match, sodium_nomatch)

plot_data = {'match': [satfat_match, calories_match, sodium_match], 'no match': [satfat_nomatch, calories_nomatch, sodium_nomatch]}
satfat = pd.DataFrame(plot_data, index = ['sat_fat', 'calories', 'sodium'])
