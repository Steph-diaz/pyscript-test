import pandas as pd
# import re
import matplotlib.pyplot as plt
import numpy as np

to_drop = ['id', 'created', 'modified', 'product_code', 'id_x', 'created_x', 'modified_x', 'category_id',
           'id_y', 'created_y', 'modified_y']

df = pd.read_csv('data/loblaws-mintel_upc_duplicates.csv').drop(columns=to_drop)
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
pyscript.write('sat-match', satfat_match)
pyscript.write('sat-noM', satfat_nomatch)

sodium_match  = len(match_df[match_df['sodium_exact_match'] == True])
sodium_nomatch = len(match_df[match_df['sodium_exact_match'] == False])
# print('sodium', sodium_match, sodium_nomatch)
pyscript.write('sod-match', sodium_match)
pyscript.write('sod-noM', sodium_nomatch)

plot_data = {'match': [satfat_match, calories_match, sodium_match], 'no match': [satfat_nomatch, calories_nomatch, sodium_nomatch]}
satfat = pd.DataFrame(plot_data, index = ['sat_fat', 'calories', 'sodium'])

###### Pandas ploting does seem to work
# pyscript.write('plot', satfat.plot.bar(rot=0))
# import matplotlib.pyplot as plt


# Bar Plot --------------------------------------------------------
labels = ['Sat Fat', 'calories', 'sodium']
match = [satfat_match, calories_match, sodium_match]
no_match = [satfat_nomatch, calories_nomatch, sodium_nomatch]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, match, width, label='Match', color= 'forestgreen')
rects2 = ax.bar(x + width/2, no_match, width, label='No Match', color='darkred')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('# of Products')
ax.set_title('Loblaws vs Mintel', pad=20)
ax.set_xticks(x, labels)
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.set_figheight(5)
fig.set_figwidth(5)

fig.tight_layout()

# plt.show()
pyscript.write('plot', fig)

# ------------------------------------------------------------------------------
# PORCENTAGES

## Creating porcentages for loblaws
total_match_loblaws = 1857

# calories
lob_percent_cal_match = round((calories_match / total_match_loblaws)*100, 2)
lob_percent_cal_nomatch = round((calories_nomatch / total_match_loblaws)*100, 2)

# saturated fat
lob_percent_sat_match = round((satfat_match / total_match_loblaws)*100, 2)
lob_percent_sat_nomatch = round((satfat_nomatch / total_match_loblaws)*100, 2)

# saturated fat
lob_percent_sod_match = round((sodium_match / total_match_loblaws)*100, 2)
lob_percent_sod_nomatch = round((sodium_nomatch / total_match_loblaws)*100, 2)

# Donut plots for percentages -------------------------------------------

# Data for plot 1 ----
match_name = 'Match: ' + str(lob_percent_sat_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_sat_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_sat_match, lob_percent_sat_nomatch]

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 1
plt.subplot(3, 1, 1)
plt.rcParams['text.color'] = 'grey'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Saturated fat', color='k')

# Data for plot 2 ----
match_name = 'Match: ' + str(lob_percent_cal_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_cal_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_cal_match, lob_percent_cal_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 2
plt.subplot(3, 1, 2)
plt.rcParams['text.color'] = 'grey'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Calories', color='k')

# Data for plot 3 ----
match_name = 'Match: ' + str(lob_percent_sod_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_sod_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_sod_match, lob_percent_sod_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 2
plt.subplot(3, 1, 3)
plt.rcParams['text.color'] = 'grey'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Sodium', color='k')


plt.subplots_adjust(left=0.2,
                    bottom=0.2,
                    right=0.8,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.4)


pyscript.write('plot2', p)
