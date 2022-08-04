import pandas as pd
# import re
import matplotlib.pyplot as plt
import numpy as np


match_df = pd.read_csv('july22_nutrient_matches_loblaws-mintel_upc_dup.csv')

# **************************** LOBLAWS DATA ***************************
x = match_df.head(3)
# pyscript.write('table', x)

size_match = len(match_df[match_df['serving_size_raw_exact_match'] == True])
size_nomatch = len(match_df[match_df['serving_size_raw_exact_match'] == False])
pyscript.write('size-match', size_match)
pyscript.write('size-noM', size_nomatch)


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

sugar_match  = len(match_df[match_df['sugar_exact_match'] == True])
sugar_nomatch = len(match_df[match_df['sugar_exact_match'] == False])
pyscript.write('sug-match', sugar_match)
pyscript.write('sug-noM', sugar_nomatch)

# plot_data = {'match': [satfat_match, calories_match, sodium_match], 'no match': [satfat_nomatch, calories_nomatch, sodium_nomatch]}
# satfat = pd.DataFrame(plot_data, index = ['sat_fat', 'calories', 'sodium'])

###### Pandas ploting does seem to work
# pyscript.write('plot', satfat.plot.bar(rot=0))
# import matplotlib.pyplot as plt


# Bar Plot --------------------------------------------------------
labels = ['Serv. Size', 'Sat Fat', 'Calories', 'Sodium', 'Sugar']
match = [size_match, satfat_match, calories_match, sodium_match, sugar_match]
no_match = [size_nomatch, satfat_nomatch, calories_nomatch, sodium_nomatch, sugar_nomatch]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/1.75, match, width, label='Match', color='#6fcb9f')
rects2 = ax.bar(x + width/1.75, no_match, width, label='No Match', color='#d64525')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('# of Products')
ax.set_title('Loblaws vs Mintel', pad=20)
ax.set_xticks(x, labels)
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)

ax.bar_label(rects1, padding=3, color='grey', fontsize=8)
ax.bar_label(rects2, padding=3, color='grey', fontsize=8)

fig.set_figheight(5)
fig.set_figwidth(5)

# fig.tight_layout()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),
          ncol=3, fancybox=True, shadow=True)

# plt.show()
pyscript.write('plot', fig)

# ------------------------------------------------------------------------------
# PORCENTAGES

# Creating porcentages for loblaws
total_match_loblaws = 1251  # 1857

# Serving size
lob_percent_size_match = round((size_match / total_match_loblaws)*100, 2)
lob_percent_size_nomatch = round((size_nomatch / total_match_loblaws)*100, 2)

# calories
lob_percent_cal_match = round((calories_match / total_match_loblaws)*100, 2)
lob_percent_cal_nomatch = round((calories_nomatch / total_match_loblaws)*100, 2)

# saturated fat
lob_percent_sat_match = round((satfat_match / total_match_loblaws)*100, 2)
lob_percent_sat_nomatch = round((satfat_nomatch / total_match_loblaws)*100, 2)

# saturated fat
lob_percent_sod_match = round((sodium_match / total_match_loblaws)*100, 2)
lob_percent_sod_nomatch = round((sodium_nomatch / total_match_loblaws)*100, 2)

# sugar
lob_percent_sug_match = round((sugar_match / total_match_loblaws)*100, 2)
lob_percent_sug_nomatch = round((sugar_nomatch / total_match_loblaws)*100, 2)

# Donut plots for percentages -------------------------------------------

# Data for plot 1 ----
match_name = 'Match: ' + str(lob_percent_size_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_size_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_size_match, lob_percent_size_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 1
plt.subplot(3, 2, 1)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, labeldistance=1.2)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Serving Size', color='k')

# Data for plot 2 ----
match_name = 'Match: ' + str(lob_percent_sat_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_sat_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_sat_match, lob_percent_sat_nomatch]

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 2
plt.subplot(3, 2, 2)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, labeldistance=0.9)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Saturated Fat', color='k')

# Data for plot 3 ----
match_name = 'Match: ' + str(lob_percent_cal_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_cal_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_cal_match, lob_percent_cal_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 3
plt.subplot(3, 2, 3)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, labeldistance=1.2)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Calories', color='k')

# Data for plot 4 ----
match_name = 'Match: ' + str(lob_percent_sod_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_sod_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_sod_match, lob_percent_sod_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 4
plt.subplot(3, 2, 4)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Sodium', color='k')

# Data for plot 5 ----
match_name = 'Match: ' + str(lob_percent_sug_match) + '%'
nomatch_name = 'No Match: ' + str(lob_percent_sug_nomatch) + '%'

names = [match_name, nomatch_name]
size = [lob_percent_sug_match, lob_percent_sug_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 4
plt.subplot(3, 2, 5)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Sugar', color='k')

plt.subplots_adjust(left=0.2,
                    bottom=0.2,
                    right=0.8,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.5)

# plt.figure(figsize=(3, 3))
pyscript.write('plot2', p)

# ************************* WALMART ***************************************
w_match_df = pd.read_csv('july22_nutrient_matches_walmart-mintel_upc_dup.csv')

w_size_match = len(w_match_df[w_match_df['serving_size_raw_exact_match']==True])
w_size_nomatch = len(w_match_df[w_match_df['serving_size_raw_exact_match']==False])
pyscript.write('w-size-match', w_size_match)
pyscript.write('w-size-noM', w_size_nomatch)

w_calories_match = len(w_match_df[w_match_df['calories_exact_match'] == True])
w_calories_nomatch = len(w_match_df[w_match_df['calories_exact_match'] == False])
pyscript.write('w-cal-match', w_calories_match)
pyscript.write('w-cal-noM', w_calories_nomatch)

w_satfat_match = len(w_match_df[w_match_df['saturatedfat_exact_match'] == True])
w_satfat_nomatch = len(w_match_df[w_match_df['saturatedfat_exact_match'] == False])
pyscript.write('w-sat-match', w_satfat_match)
pyscript.write('w-sat-noM', w_satfat_nomatch)

w_sodium_match = len(w_match_df[w_match_df['sodium_exact_match'] == True])
w_sodium_nomatch = len(w_match_df[w_match_df['sodium_exact_match'] == False])
pyscript.write('w-sod-match', w_sodium_match)
pyscript.write('w-sod-noM', w_sodium_nomatch)

w_sugar_match = len(w_match_df[w_match_df['sugar_exact_match'] == True])
w_sugar_nomatch = len(w_match_df[w_match_df['sugar_exact_match'] == False])
pyscript.write('w-sug-match', w_sugar_match)
pyscript.write('w-sug-noM', w_sugar_nomatch)

# Pandas plot
# w_plot_data = {'match': [w_size_match, w_satfat_match, w_calories_match, w_sodium_match], 'no match': [w_size_nomatch, w_satfat_nomatch, w_calories_nomatch, w_sodium_nomatch]}
# w_plot_df = pd.DataFrame(w_plot_data, index = ['Serving Size', 'sat_fat', 'calories', 'sodium'])


# Bar Plot --------------------------------------------------------
labels = ['Serv. Size', 'Sat Fat', 'Calories', 'Sodium', 'Sugar']
w_match = [w_size_match, w_satfat_match, w_calories_match, w_sodium_match, w_sugar_match]
w_no_match = [w_size_nomatch, w_satfat_nomatch, w_calories_nomatch, w_sodium_nomatch, w_sugar_nomatch]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/1.75, w_match, width, label='Match', color='#6fcb9f')
rects2 = ax.bar(x + width/1.75, w_no_match, width, label='No Match', color='#d64525')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('# of Products')
ax.set_title('Walmart vs Mintel', pad=20, color='black')
ax.set_xticks(x, labels)
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)

ax.bar_label(rects1, padding=3, color='grey', fontsize=8)
ax.bar_label(rects2, padding=3, color='grey', fontsize=8)

fig.set_figheight(5)
fig.set_figwidth(5)

# fig.tight_layout()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),
          ncol=3, fancybox=True, shadow=True)

# plt.show()
pyscript.write('w-plot', fig)


# ------------------------------------------------------------------------------
# PORCENTAGES

# Creating porcentages for walmart
total_match_walmart = 1293

# Serving size
wal_percent_size_match = round((w_size_match / total_match_walmart)*100, 2)
wal_percent_size_nomatch = round((w_size_nomatch / total_match_walmart)*100, 2)

# calories
wal_percent_cal_match = round((w_calories_match / total_match_walmart)*100, 2)
wal_percent_cal_nomatch = round((w_calories_nomatch / total_match_walmart)*100, 2)

# saturated fat
wal_percent_sat_match = round((w_satfat_match / total_match_walmart)*100, 2)
wal_percent_sat_nomatch = round((w_satfat_nomatch / total_match_walmart)*100, 2)

# saturated fat
wal_percent_sod_match = round((w_sodium_match / total_match_walmart)*100, 2)
wal_percent_sod_nomatch = round((w_sodium_nomatch / total_match_walmart)*100, 2)

# sugar
wal_percent_sug_match = round((w_sugar_match / total_match_walmart)*100, 2)
wal_percent_sug_nomatch = round((w_sugar_nomatch / total_match_walmart)*100, 2)

# Donut plots for percentages -------------------------------------------

# Data for plot 1 ----
match_name = 'Match: ' + str(wal_percent_size_match) + '%'
nomatch_name = 'No Match: ' + str(wal_percent_size_nomatch) + '%'

names = [match_name, nomatch_name]
size = [wal_percent_size_match, wal_percent_size_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 1
plt.subplot(3, 2, 1)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Serving Size', color='k')

# Data for plot 2 ----
match_name = 'Match: ' + str(wal_percent_sat_match) + '%'
nomatch_name = 'No Match: ' + str(wal_percent_sat_nomatch) + '%'

names = [match_name, nomatch_name]
size = [wal_percent_sat_match, wal_percent_sat_nomatch]

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 2
plt.subplot(3, 2, 2)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Saturated Fat', color='k')

# Data for plot 3 ----
match_name = 'Match: ' + str(wal_percent_cal_match) + '%'
nomatch_name = 'No Match: ' + str(wal_percent_cal_nomatch) + '%'

names = [match_name, nomatch_name]
size = [wal_percent_cal_match, wal_percent_cal_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 3
plt.subplot(3, 2, 3)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Calories', color='k')

# Data for plot 4 ----
match_name = 'Match: ' + str(wal_percent_sod_match) + '%'
nomatch_name = 'No Match: ' + str(wal_percent_sod_nomatch) + '%'

names = [match_name, nomatch_name]
size = [wal_percent_sod_match, wal_percent_sod_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 4
plt.subplot(3, 2, 4)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Sodium', color='k')

# Data for plot 5 ----
match_name = 'Match: ' + str(wal_percent_sod_match) + '%'
nomatch_name = 'No Match: ' + str(wal_percent_sod_nomatch) + '%'

names = [match_name, nomatch_name]
size = [wal_percent_sug_match, wal_percent_sug_nomatch]

my_circle = plt.Circle((0, 0), 0.7, color='white')

# position 5
plt.subplot(3, 2, 5)
plt.rcParams['text.color'] = 'grey'
plt.rcParams['font.size'] = '8.5'
plt.pie(size, labels=names, colors=['forestgreen', 'darkred'],
        wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Sugar', color='k')


plt.subplots_adjust(left=0.2,
                    bottom=0.2,
                    right=0.8,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.4)

# plt.figure(figsize=(3, 3))
pyscript.write('w-plot2', p)
