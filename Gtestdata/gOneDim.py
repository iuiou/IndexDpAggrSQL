import random

import pandas as pd
import numpy as np

# 10^6*20
df = pd.DataFrame(columns=['name', 'income', 'age'])
namelist = list()
incomelist = list()
agelist = list()

num = 0
while True:
    income = random.randint(0,200000)
    sumnum = random.randint(1, 20)
    for j in range(sumnum):
        num = num + 1
        age = random.randint(0,30)
        namelist.append('fzh')
        incomelist.append(income)
        agelist.append(age)
        if num == 5000000:
            break
    if num == 5000000:
        break

df = pd.DataFrame({'name' : namelist, 'income' : incomelist, 'age' : agelist})
df.to_csv('oneDimData.csv', index=False)
print("finished" + str(num))