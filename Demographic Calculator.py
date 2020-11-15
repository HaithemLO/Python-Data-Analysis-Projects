import pandas as  pd
import numpy as np

df = pd.read_csv (r'C:\Users\haith\Desktop\Programming Stuff\Python\Projects\Data Analysis with Python Projects\Demographic Data Analyzer\adult.data.csv')


#Finds out how many people are in each race

d = dict()

for word in df['race']:
    if word in d:
        d[word] = d[word] + 1

    else:
        d[word] = 1

for key in list(d.keys()):
    print(key,":",d[key])


##finds out the average age of men

Males = df[df.sex=='Male']
print("The average age of Males is ",Males['age'].mean())

##Finds out percentage of people with bachelors
a = 0
for x in df['education']:
    if x == 'Bachelors' :
        a+=1
print("The percentage of people who have bachelors is",(a/df.shape[0])*100,"%")

## works out earning of higher education
higher_edu_num = df.loc[(df['education'] == 'Bachelors')| (df['education'] == 'Masters') | (df['education'] == 'Doctorate') ]


higher_edu_num2 = higher_edu_num.loc[(higher_edu_num['salary'] == '>50K')]

print("The percentage of people who have a higher education and are making >50K is",(higher_edu_num2.shape[0]/higher_edu_num.shape[0])*100,"%")

## Percentage of people without advanced education make more than 50K

a = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') ]
b= (a.loc[(a['salary'] == '>50K')]).shape[0]
a = a.shape[0]
print("The Percentage of people without advanced education making more than 50K",b/a*100,"%")

## Minimum hours worked

a = df['hours-per-week'].min()
print(a,'Is the minimum number of hours worked')

##Minimum hours and >50K

a = df.loc[(df['hours-per-week'] == 1)]
b = a.loc[(a['salary'] == '>50K')]
aa=a.shape[0]
bb=b.shape[0]

print(bb/aa*100,"% of people who work minimum hours make >50K")

## Country with the highest number of >50K earners
temp0 = {}
d = dict()

for word in df['native-country']:
    if word in d:
        d[word] = d[word] + 1

    else:
        d[word] = 1

for key in list(d.keys()):
    k = (key,d[key])
    temp0.__setitem__(key,d[key])




a = df.loc[(df['salary'] == '>50K')]
temp1 = {}
d = dict()

for word in a['native-country']:
    if word in d:
        d[word] = d[word] + 1

    else:
        d[word] = 1

for key in list(d.keys()):
   
    temp1.__setitem__(key,d[key])



c={}

for x in temp0:
    if x in temp1:
        c.__setitem__(x,((temp1[x]/temp0[x])*100))


largest = 0
for x in c:
    if c[x] > largest:
        largest = c[x]
        country = x


print("The country with the highest percentage of high earners is",country,"with",largest,"% of earners making >50K")


##Most common occupation of high earners in india

a = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

d = dict()
c = {}
for word in a['occupation']:
    if word in d:
        d[word] = d[word] + 1

    else:
        d[word] = 1

for key in list(d.keys()):
    c.__setitem__(key,d[key])


largest = 0
for x in c:
    if c[x] > largest:
        largest = c[x]
        country = x
print("The most common occupation for high earners in India is",country)











