import pandas as pd
import time
from Query.aggrQuery import segTAggrQuery

class allSegmentTQuery:
    def __init__(self, joinnum, indexlist, aggrtype):
        self.mp = {}
        for i in range(joinnum):
            id = i+1
            dirn = 'Index/indexfor' + str(id) + '.csv'
            self.mp[id] = segTAggrQuery(dirn, indexlist) # 参与方id map到aggrQuery
        self.aggrType = aggrtype