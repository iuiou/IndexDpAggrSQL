import random

import pandas as pd
import numpy as np

# 10^6*20
df = pd.DataFrame(columns=['name', 'income', 'age'])
namelist = list()
incomelist = list()
agelist = list()

person = [1, 3, 10, 100, 1000]

num = 0
while True:
    income = np.random.randint(0,200000)
    sumnum = np.random.randint(1, 20)
    age = np.random.normal(38,12.5,sumnum)
    for j in range(sumnum):
        num = num + 1
        namelist.append('fzh')
        incomelist.append(income)
        agelist.append(int(age[j]))
        if num == 3000000:
            break
    if num == 3000000:
        break

df = pd.DataFrame({'name' : namelist, 'income' : incomelist, 'age' : agelist})
df.to_csv('oneDimData.csv', index=False)
print("finished" + str(num))