import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt


df = pd.read_csv (r'medical_examination.csv')


#Adds an overweight column
a = (df['weight']/((df['height']/100)**2)) 

overweight = []

for x in a :
    if x >25:
        overweight.append(1)
    else :
        overweight.append(0)
df['Overweight'] = overweight


#Normalises the data (replaces 2 with 1 and 1 with 0) for chol and gluc
new = []
for x in df.cholesterol:
    x -=1
    while x >1:
        x-=1
    new.append(x)
df['cholesterol'] = new


new = []
for x in df.gluc:
    x -=1
    while x >1:
        x-=1
    new.append(x)
df['gluc'] = new

#Graph values
No_Cardio = df.loc[(df['cardio'] == 0)]
#active
active0 = (No_Cardio.loc[(No_Cardio['active'] ==0)]).shape[0]
active1 = (No_Cardio.loc[(No_Cardio['active'] ==1)]).shape[0]
#alco
alco0 = (No_Cardio.loc[(No_Cardio['alco'] ==0)]).shape[0]
alco1 = (No_Cardio.loc[(No_Cardio['alco'] ==1)]).shape[0]
#cholesterol
chol0 = (No_Cardio.loc[(No_Cardio['cholesterol'] ==0)]).shape[0]
chol1 = (No_Cardio.loc[(No_Cardio['cholesterol'] ==1)]).shape[0]
#gluc
gluc0 = (No_Cardio.loc[(No_Cardio['gluc'] ==0)]).shape[0]
gluc1 = (No_Cardio.loc[(No_Cardio['gluc'] ==1)]).shape[0]
#overweight
overweight0 =(No_Cardio.loc[(No_Cardio['Overweight'] ==0)]).shape[0]
overweight1 =(No_Cardio.loc[(No_Cardio['Overweight'] ==1)]).shape[0]
#smoke
smoke0 =(No_Cardio.loc[(No_Cardio['smoke'] ==0)]).shape[0]
smoke1 =(No_Cardio.loc[(No_Cardio['smoke'] ==1)]).shape[0]

#Graph values
Yes_Cardio = df.loc[(df['cardio'] == 1)]
#active
active00 = (Yes_Cardio.loc[(Yes_Cardio['active'] ==0)]).shape[0]
active11 = (Yes_Cardio.loc[(Yes_Cardio['active'] ==1)]).shape[0]
#alco
alco00 = (Yes_Cardio.loc[(Yes_Cardio['alco'] ==0)]).shape[0]
alco11 = (Yes_Cardio.loc[(Yes_Cardio['alco'] ==1)]).shape[0]
#cholesterol
chol00 = (Yes_Cardio.loc[(Yes_Cardio['cholesterol'] ==0)]).shape[0]
chol11 = (Yes_Cardio.loc[(Yes_Cardio['cholesterol'] ==1)]).shape[0]
#gluc
gluc00 = (Yes_Cardio.loc[(Yes_Cardio['gluc'] ==0)]).shape[0]
gluc11 = (Yes_Cardio.loc[(Yes_Cardio['gluc'] ==1)]).shape[0]
#overweight
overweight00 =(Yes_Cardio.loc[(Yes_Cardio['Overweight'] ==0)]).shape[0]
overweight11 =(Yes_Cardio.loc[(Yes_Cardio['Overweight'] ==1)]).shape[0]
#smoke
smoke00 =(Yes_Cardio.loc[(Yes_Cardio['smoke'] ==0)]).shape[0]
smoke11 =(Yes_Cardio.loc[(Yes_Cardio['smoke'] ==1)]).shape[0]






#creating a graph


# objects = ('active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke')

# Negative = (active0,alco0,chol0,gluc0,overweight0,smoke0)
# Positive = (active1,alco1,chol1,gluc1,overweight1,smoke1)

# ind = np.arange(len(Negative))  # the x locations for the groups
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(ind - width/2, Negative, width, 
#                 label='Negative X-Axis')
# rects2 = ax.bar(ind + width/2, Positive, width, 
#                 label='Positive X-Axis')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Total Number of people')
# ax.set_title('No Cardio')
# ax.set_xticks(ind)
# ax.set_xticklabels(('active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'))
# ax.legend()





# objects = ('active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke')

# Negative = (active00,alco00,chol00,gluc00,overweight00,smoke00)
# Positive = (active11,alco11,chol11,gluc11,overweight11,smoke11)

# ind = np.arange(len(Negative))  # the x locations for the groups
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(ind - width/2, Negative, width, 
#                 label='Negative X-Axis')
# rects2 = ax.bar(ind + width/2, Positive, width, 
#                 label='Positive X-Axis')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Total Number of people')
# ax.set_title('No Cardio')
# ax.set_xticks(ind)
# ax.set_xticklabels(('active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'))
# ax.legend()


# plt.show()

#Cleaning the data
a = df.loc[(df['ap_lo'] <= df['ap_hi'])]
b = a.loc[(a['height'] >= a['height'].quantile(0.025))]
c = b.loc[(b['height'] <= b['height'].quantile(0.975))]
d = c.loc[(c['weight'] >= c['weight'].quantile(0.025))]
e = d.loc[(d['weight'] <= d['weight'].quantile(0.975))]



corrMatrix = e.corr()
corr = corrMatrix.round(decimals=1)
# sn.heatmap(f,annot=True)

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sn.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sn.heatmap(corr, mask=mask, vmax=.3, square=True)

print(f)
plt.show()
