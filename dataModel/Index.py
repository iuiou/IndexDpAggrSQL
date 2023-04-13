import pandas as pd
import numpy as np


class SegmentSet:
    def __init__(self, seglist):
        self.seglist = seglist
        self.num = len(seglist)

    def __eq__(self, seg):
        if self.num != seg.num:
            return False
        for i in range(self.num):
            if self.seglist[i] != seg.seglist[i]:
                return False
        return True

    def __hash__(self):
        ans = str()
        for element in self.seglist:
            ans = ans + str(element)
        return hash(ans)

class CustomIndex:
    def __init__(self, raw_data : pd.DataFrame, IndexKeySet, aggrType, target):
        self.index = dict()
        self.otherInf = dict()
        self.namelist = IndexKeySet
        self.aggrType = aggrType
        nums = len(raw_data)
        for i in range(nums):
            nameSet = list()
            for name in IndexKeySet:
                nameSet.append(raw_data[name].iloc[i])
            nameSet = SegmentSet(nameSet)
            if nameSet not in self.index:
                self.index[nameSet] = 0
            if aggrType == "Sum":
                value = int(raw_data[target].iloc[i])
                self.index[nameSet] += value
                self.otherInf[nameSet] = max(self.otherInf[nameSet], value)
            elif aggrType == "Count":
                self.index[nameSet] += 1

    def IndextoDataFrame(self, addnoise, eps):
        Nametolist = dict()
        for name in self.namelist:
            Nametolist[name] = list()
        Nametolist['aggr'] = list()
        for key in self.index:
            keylist = key.seglist
            i = 0
            for value in keylist:
                Nametolist[self.namelist[i]].append(value)
                i = i + 1
            if addnoise:
                if self.aggrType == "Sum":
                    Nametolist['aggr'].append(
                        self.index[key] + np.random.laplace(0, self.otherInf[key]/eps))
                elif self.aggrType == "Count":
                    Nametolist['aggr'].append(
                        self.index[key] + np.random.laplace(0, 1/eps))
            else:
                Nametolist['aggr'].append(self.index[key])
        return pd.DataFrame(Nametolist)


class SegmentTIndex:
    def __index__(self):
        pass