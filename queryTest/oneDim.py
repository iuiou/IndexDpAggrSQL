import random

import pandas as pd
import numpy as np
from queryTest.aggrQuery import aggrQuery

customIndex = "../Gtestdata/Indexresult/oneDimIndex.csv"
indexWithNoise = "../Gtestdata/Indexresult/noisyOneDimIndex.csv"

ci = aggrQuery(customIndex, ['income'])
iwn = aggrQuery(indexWithNoise, ['income'])

vol = [0.1, 0.3, 0.5, 0.8]
mx = 200000
for num in vol:
    sumRelerror = 0
    sumrel = 0
    for i in range(30):
        len = int(mx * num)
        l = random.randint(0, mx-len)
        r = l + len
        condition = {
            "income" : (l,r)
        }
        ans1 = ci.Customquery(condition, 'Count')
        sumrel += ans1 / len
        print(str(l) + ' ' + str(r) + ' ' + str(ans1))
        # ans2 = iwn.Customquery(condition, 'Count')
        # relerror = abs(ans1 - ans2)/ans1
        # sumRelerror += relerror
    # sumRelerror /= 30
    print(str(num) + ':' + str(sumrel))





