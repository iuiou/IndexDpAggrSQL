import random

import pandas as pd
import numpy as np
from queryTest.aggrQuery import aggrQuery

customIndex = "../Gtestdata/Indexresult/oneDimIndex.csv"
indexWithNoise = "../Gtestdata/Indexresult/noisyOneDimIndex.csv"

ci = aggrQuery(customIndex, ['income'])
iwn = aggrQuery(indexWithNoise, ['income'])

# vol = [0.0001, 0.001, 0.01, 0.1]
# mx = 200000
# for num in vol:
#     sumRelerror = 0
#     sumrel = 0
#     for i in range(300):
#         len = int(mx * num)
#         l = random.randint(0, mx-len)
#         r = l + len
#         condition = {
#             "income" : (l,r)
#         }
#         ans1 = ci.Customquery(condition, 'Count')
#         # sumrel += ans1 / len
#         # print(str(l) + ' ' + str(r) + ' ' + str(ans1))
#         ans2 = iwn.Customquery(condition, 'Count')
#         # print(str((l,r)) + ':' + str(ans1) + ' ' + str(ans2))
#         relerror = abs(ans1 - ans2)/ans1
#         sumRelerror += relerror
#     sumRelerror /= 300
#     print(str(num) + ':' + str(sumRelerror))


print(ci.Customquery({"income":(76069, 152136)}, 'Count'))



