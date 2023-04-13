import pandas as pd


class aggrQuery:
    def __init__(self, indexFile, indexList):
        self.data = pd.read_csv(indexFile, header=0)
        self.indexList = indexList

    def Customquery(self, conditionlist, aggrType):
        nums = len(self.data)
        ans = 0
        for i in range(nums):
            select = True
            for name in conditionlist:
                value = self.data[name].iloc[i]
                if not (value >= conditionlist[name][0] \
                        and value <= conditionlist[name][1]):
                    select = False
                    break
                if select:
                    if aggrType == 'Sum' or aggrType == 'Count':
                        ans = ans + float(self.data['aggr'].iloc[i])
                    elif aggrType == 'Max':
                        ans = max(ans, float(self.data['aggr'].iloc[i]))
                    elif aggrType == 'Min':
                        ans = min(ans, float(self.data['aggr'].iloc[i]))
                    else:
                        pass
        return ans
