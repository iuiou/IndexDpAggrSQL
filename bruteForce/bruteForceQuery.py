import pandas as pd
import time
from Query.aggrQuery import aggrQuery

class BruteForce:
    def __init__(self, joinnum, indexlist, aggrtype):
        self.mp = {}
        for i in range(joinnum):
            id = i+1
            dirn = 'Index/indexfor' + str(id) + '.csv'
            self.mp[id] = aggrQuery(dirn, indexlist) # 参与方id map到aggrQuery
        self.aggrType = aggrtype


    def cal(self, qu):
        t = 0
        ans = 0
        for name in self.mp:
            t1 = time.perf_counter()
            ans += self.mp[name].Customquery(qu, self.aggrType)
            t2 = time.perf_counter()
            t = max(t, t2-t1)
        return (ans,t)


bf = BruteForce(3, ['a', 'b'], 'Sum')
qu = {
    'a' : (100,999),
    'b' : (10,99)
}
print(bf.cal(qu))