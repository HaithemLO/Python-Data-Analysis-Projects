import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import 
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from scipy import stats

def draw_plot():

    # Read data from file
  df = pd.read_csv (r'epa-sea-level.csv')

  x=df['Year']
  y=df['CSIRO Adjusted Sea Level']

  ##Finds the line of regression 1990-2050

  slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
  # print("slope: %f  intercept:%f"  % (slope,intercept))

  x2 = list(range(1880,2050))
  y2 = []

  for temp in x2:
      y2.append(intercept+slope*temp)

  ##Finds second Line of regression
  a = df.loc[(df['Year'] >1999)]
  x3=a['Year']
  y3=a['CSIRO Adjusted Sea Level']

  slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x3,y3)
  x4 = list(range(1880,2050))
  y4 = []

  for temp in x4:
      y4.append(intercept2+slope2*temp)


  fig,ax = plt.subplots()
  ax.plot(x,y,label='original data')
  ax.plot(x2,y2,'r',label='First Regression line')
  ax.plot(x4,y4,'cyan',label='Second Regression line')
  ax.legend()
  ax.set(xlabel='Year',ylabel='Sea Level (inches)',title='Rise in Sea Level')

  ax.grid()
  plt.show()



  fig.savefig("test2.png")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()