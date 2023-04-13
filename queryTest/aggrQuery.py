import pandas as pd


class aggrQuery:
    def __init__(self, indexFile, indexList):
        self.data = pd.read_csv(indexFile, header=0)
        self.indexList = indexList


