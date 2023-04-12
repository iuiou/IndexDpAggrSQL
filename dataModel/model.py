import pandas as pd
import numpy as np


class attr:
    def __init__(self, name, type, raw_data):
        self.name = name
        self.type = type
        self.dcarray = list()
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
        self.dcarray.insert(0, 0)  # insert 0 into begin

class table:
    def __init__(self, name, schema, raw_data):
        self.name = name
        self.schema = schema
        self.data = dict()
        self.indexKeySet = list()
        for key in schema.keys():
            self.data[key] = attr(key, schema[key]["type"], raw_data)
            if schema[key]["NeedIndex"] == True:
                self.indexKeySet.append(key)

    def getAttr(self, name):
        return self.data[name]

    # def create_costom_index(self, target, aggr):
    #     for name in self.indexKeySet:




