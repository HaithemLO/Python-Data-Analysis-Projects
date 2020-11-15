import numpy as np
import statistics as st
import math as math

def calculate(list):
    calculations = {
    'mean':[],
    'variance':[],
    'standard deviation':[],
    'max':[],
    'min':[],
    'sum':[]}

    if len(list) != 9:
        return "Need 9 values in the array"

    a = np.array(list)
    b=a.reshape(3,3)

    i = 0

    #Working out the mean
    while i < 2:
        mean = []
        c=b.sum(axis = i)/3
        e = c.flatten(order='C')
        for x in e:
            mean.append(x)

        calculations['mean'].append(mean)
        i +=1

    #working out the total mean
    mean = 0
    for x in list:
        mean +=x
    calculations['mean'].append(mean/9)

    ##VARIANCE
    #Working out the variance for columns
    temp = []
    i = 0
    while i < 3 :
        data = b[:,i]
        n = len(data)
        mean = sum(data) / n
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / n
        temp.append(variance)
        i+=1
    calculations['variance'].append(temp)


    #Working out the variance for rows
    temp = []
    i = 0
    while i < 3 :
        data = b[i]
        n = len(data)
        mean = sum(data) / n
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / n
        temp.append(variance)
        i+=1
    calculations['variance'].append(temp)

    #Total variance

    data = list
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    calculations['variance'].append(variance)

    ##STANDARD DEVIATION
    i=0
    while i < 2:
        temp = []
        for x in calculations['variance'][i] :
            temp.append(math.sqrt(x))
        calculations['standard deviation'].append(temp)
        i+=1

    calculations['standard deviation'].append(math.sqrt(calculations['variance'][2]))



    # Maximum Value
    #columns
    temp = []
    i = 0
    while i < 3 :
        data = max(b[:,i])
        temp.append(data)
        i+=1
    calculations['max'].append(temp)

    #rows
    temp = []
    i = 0
    while i < 3 :
        data = max(b[i])
        temp.append(data)
        i+=1
    calculations['max'].append(temp)

    calculations['max'].append(max(list))


    # Minimum Value
    #columns
    temp = []
    i = 0
    while i < 3 :
        data = min(b[:,i])
        temp.append(data)
        i+=1
    calculations['min'].append(temp)

    #rows
    temp = []
    i = 0
    while i < 3 :
        data = min(b[i])
        temp.append(data)
        i+=1
    calculations['min'].append(temp)

    calculations['min'].append(min(list))


    i = 0
    while i<2: 
        temp = []
        c=b.sum(axis = i)
        d=c.flatten(order='C')
        for x in d:
            temp.append(x)
        calculations['sum'].append(temp)
        i+=1

    temp = 0
    for x in list:
        temp += x

    calculations['sum'].append(temp)




    return calculations

print(calculate([1,2,3,4,5,6,7,8]))
