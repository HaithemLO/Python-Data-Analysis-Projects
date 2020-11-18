import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates
import re

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv (r'fcc-forum-pageviews.csv')
a = df.set_index('date')
b = a.loc[(a['value'] >= a['value'].quantile(0.025))]
c = b.loc[(b['value'] <= b['value'].quantile(0.975))]

dates = c.index

def draw_line_plot():
    # Draw line plot
    fig = plt.figure()

    ax1 = fig.add_subplot()
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Date')
    ax1.set_title('Daily freeCodeCamp Forum Page views 5/2016-12/2019')
    date_objects = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
    plt.plot(date_objects,c['value'])

    plt.show()





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

  # Copy and modify data for monthly bar plot
  months = ['01','02','03','04','05','06','07','08','09','10','11','12']
  years = ['2016','2017','2018','2019']

  ylen = 0

  Total1=[]

  while ylen < 4:
      mlen = 0
      Total = []
      while mlen < 12 :
          temp = 0
          temp2 = 0
          for x in c.index:
              if re.search("^"+years[ylen]+"."+months[mlen],x):
                  temp2 += 1
                  temp += c.loc[x,'value']
          if temp2 == 0:
              temp2 = 1
          Total.append(temp/temp2)
          mlen +=1  
      Total1.append(Total)    
      ylen += 1



  New_Total = []


  mlen = 0

  while mlen < 12 :
      temp = []
      ylen = 0

      while ylen < 4 :
          
          temp.append(Total1[ylen][mlen])
          ylen+=1
      New_Total.append(temp)
      mlen += 1
  


    # Draw bar plot
  barWidth = 0.05

  r1 = np.arange(len(New_Total[0]))
  r2 = [x + barWidth for x in r1]
  r3 = [x + barWidth for x in r2]
  r4 = [x + barWidth for x in r3]
  r5 = [x + barWidth for x in r4]
  r6 = [x + barWidth for x in r5]
  r7 = [x + barWidth for x in r6]
  r8 = [x + barWidth for x in r7]
  r9 = [x + barWidth for x in r8]
  r10 = [x + barWidth for x in r9]
  r11 = [x + barWidth for x in r10]
  r12 = [x + barWidth for x in r11]

  plt.bar(r1, New_Total[0], color='#7f6d5f', width=barWidth, edgecolor='white', label='January')
  plt.bar(r2, New_Total[1], color='#557f2d', width=barWidth, edgecolor='white', label='February')
  plt.bar(r3, New_Total[2], color='#E9D66B', width=barWidth, edgecolor='white', label='March')
  plt.bar(r4, New_Total[3], color='#0048BA', width=barWidth, edgecolor='white', label='April')
  plt.bar(r5, New_Total[4], color='#7CB9E8', width=barWidth, edgecolor='white', label='May')
  plt.bar(r6, New_Total[5], color='#00FFFF', width=barWidth, edgecolor='white', label='June')
  plt.bar(r7, New_Total[6], color='#B284BE', width=barWidth, edgecolor='white', label='July')
  plt.bar(r8, New_Total[7], color='#D0FF14', width=barWidth, edgecolor='white', label='August')
  plt.bar(r9, New_Total[8], color='#C46210', width=barWidth, edgecolor='white', label='September')
  plt.bar(r10, New_Total[9], color='#E52B50', width=barWidth, edgecolor='white', label='October')
  plt.bar(r11, New_Total[10], color='#9F2B68', width=barWidth, edgecolor='white', label='November')
  plt.bar(r12, New_Total[11], color='#F19CBB', width=barWidth, edgecolor='white', label='December')


  plt.ylabel('Page Visits', fontweight='bold')
  plt.xlabel('Year', fontweight='bold')
  plt.xticks([r + barWidth for r in range(len(New_Total[0]))], ['2016', '2017', '2018', '2019'])

  plt.legend()
  fig = plt.show()





    # Save image and return fig (don't change this part)
    # fig.savefig('bar_plot.png')
    # return fig

def draw_box_plot():

   ##Adds the Year column to the Dataframe
  temp = []
  for x in c.index:
      if re.search("^2016",x):
          temp.append("2016")
      elif re.search("^2017",x):
          temp.append("2017")
      elif re.search("^2018",x):
          temp.append("2018")
      elif re.search("^2019",x):
          temp.append("2019")

  c['year'] = temp

  sns.set_style("whitegrid")

  ##Adds a month column
  months2 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

  temp2=[]

  for x in c.index:
      temp2.append(months2[int(x.split('-')[1])-1])
  c['month'] = temp2




  ##Displays the graph
  fig, axs = plt.subplots(ncols=2)
  ax1=sns.boxplot(x='month', y="value", data=c,ax=axs[1])

  ax2=sns.boxplot(x='year', y="value", data=c,ax=axs[0])
  ax1.set(ylim=(0, 190000))
  ax2.set(ylim=(0, 190000))
  ax1.set(xlabel='Month', ylabel='Page Views')
  ax2.set(xlabel='Year', ylabel='Page Views')
  plt.show()
    # fig.savefig('box_plot.png')
    # return fig
