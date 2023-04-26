import pandas as pd
import numpy as np
from dataModel.Index import CustomIndex
from dataModel.Index import SegmentTIndex


class attr:
    def __init__(self, name, type, raw_data):
        self.name = name
        self.type = type
        self.dcarray = list()
        self.mp = dict()
        if type == 'int':
            self.array = list(map(int, raw_data[name].values.tolist()))
        elif type == 'float':
            self.array = list(map(float, raw_data[name].values.tolist()))
        elif type == 'str':
            self.array = list(map(str, raw_data[name].values.tolist()))
        else:
            print('error,no such data type')
        self.discretize()

    def index(self, row_idx : int):
        return self.array[row_idx]

    def discretize(self):
        if type == "str":
            return
        self.dcarray = list(set(self.array))
        self.dcarray.sort()
        rk = 1
        for num in self.dcarray:
            self.mp[num] = rk
            rk = rk + 1
        self.dcarray.insert(0, 0)  # insert 0 into begin, first number is dcarray[1]


class table:
    def __init__(self, name, schema, raw_data):
        self.name = name
        self.schema = schema
        self.data = dict() # name to attribute
        self.indexKeySet = list()
        self.raw_data = raw_data
        for key in list(self.raw_data):
            self.data[key] = attr(key, schema[key]["type"], raw_data)
            if schema[key]["NeedIndex"] == True:
                self.indexKeySet.append(key)

    def getAttr(self, name):
        return self.data[name]

    def create_costom_index(self, target, aggr, eps, targetRoot):
        customIndex = CustomIndex(self.raw_data, self.indexKeySet, aggr, target)
        noisyIndexFrame = customIndex.IndextoDataFrame(addnoise=True, eps=eps)
        noisyIndexFrame.to_csv(targetRoot, index=False)

    def create_SegmentT_index(self, target, aggr, eps, targetRoot):
        segmentTIndex = SegmentTIndex(self.data, self.indexKeySet)
        segmentTIndex.buildIndex(aggr, target)
        noisyIndexFrame = segmentTIndex.IndextoDataFrame(addnoise=True, eps=eps)
        noisyIndexFrame.to_csv(targetRoot, index=False)

    def create_normal_index(self, target, aggr, targetRoot):
        normalIndex = CustomIndex(self.raw_data, self.indexKeySet, aggr, target)
        indexFrame = normalIndex.IndextoDataFrame(addnoise=False, eps = 0)
        indexFrame.to_csv(targetRoot, index=False)










