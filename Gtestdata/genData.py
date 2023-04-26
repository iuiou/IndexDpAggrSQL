import random

import pandas as pd
import numpy as np

class DataGenerator:
    def __init__(self, datamp):
        self.datamp = datamp

    def gen(self, num, joinnum):
        ans = {}
        for i in range(joinnum):
            ans[i+1] = {}
        for i in range(joinnum):
            for name in self.datamp:
                ans[i+1][name] = []
            ans[i+1]['d'] = list()
        for i in range(num):
            select = np.random.randint(1, joinnum + 1)
            for name in self.datamp:
                mn = 1
                mx = self.datamp[name]
                mid = (mn + mx) / 2
                sigma = (mx - mid) / 3
                ans[select][name].append(int(np.random.normal(mid, sigma)))
            ans[select]['d'].append(int(np.random.normal(38, 12.5)))
        dirpath = 'data/testdatafor'
        for i in range(joinnum):
            itsdirpath = dirpath + str(i+1) + '.csv'
            df = pd.DataFrame(ans[i+1])
            df.to_csv(itsdirpath, index=False)



datamp = {
    'a' : 1024,
    'b' : 256
}
g = DataGenerator(datamp)
g.gen(3000000, 3)
# 10^6*20
# df = pd.DataFrame(columns=['name', 'income', 'age'])
# namelist = list()
# incomelist = list()
# agelist = list()
#
# person = [1, 3, 10, 100, 1000]
#
# num = 0
# while True:
#     income = np.random.randint(0,200000)
#     sumnum = np.random.randint(1, 20)
#     age = np.random.normal(38,12.5,sumnum)
#     for j in range(sumnum):
#         num = num + 1
#         namelist.append('fzh')
#         incomelist.append(income)
#         agelist.append(int(age[j]))
#         if num == 3000000:
#             break
#     if num == 3000000:
#         break
#
# df = pd.DataFrame({'name' : namelist, 'income' : incomelist, 'age' : agelist})
# df.to_csv('oneDimData.csv', index=False)
# print("finished" + str(num))