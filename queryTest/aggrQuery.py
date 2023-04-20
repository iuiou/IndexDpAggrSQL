import pandas as pd
from dataModel.Index import SegmentSet

class Query:
    def __init__(self, indexFile, indexList):
        self.data = pd.read_csv(indexFile, header=0)
        self.indexList = indexList
        self.index = dict()
        nums = len(self.data)
        for i in range(nums):
            nameSet = list()
            for name in indexList:
                nameSet.append(str(self.data[name].iloc[i]))
            nameSet = SegmentSet(nameSet)
            self.index[nameSet] = self.data['aggr'].iloc[i]

    def cal(self, nameSet, aggrType, last):
        ans = 0
        if nameSet in self.index:
            if aggrType == 'Sum' or aggrType == 'Count':
                ans = last + float(self.index[nameSet])
            elif aggrType == 'Max':
                ans = max(last, float(self.index[nameSet]))
            elif aggrType == 'Min':
                ans = min(last, float(self.index[nameSet]))
        return ans



class aggrQuery(Query):
    def __init__(self, indexFile, indexList):
        super().__init__(indexFile, indexList)

    def Customquery(self, conditionlist, aggrType):
        ans = 0
        conNum = len(self.indexList)
        if conNum == 1:
            mn = conditionlist[self.indexList[0]][0]
            mx = conditionlist[self.indexList[0]][1]
            for i in range(mn,mx+1,1):
                nameSet = SegmentSet([str(i)])
                ans = self.cal(nameSet, aggrType, ans)
        elif conNum == 2:
            mn1 = conditionlist[self.indexList[0]][0]
            mx1 = conditionlist[self.indexList[0]][1]
            mn2 = conditionlist[self.indexList[1]][0]
            mx2 = conditionlist[self.indexList[1]][1]
            for i in range(mn1,mx1+1,1):
                for j in range(mn2,mx2+1,1):
                    nameSet = SegmentSet([str(i),str(j)])
                    if nameSet in self.index:
                        ans = self.cal(nameSet, aggrType, ans)
        elif conNum == 3:
            mn1 = conditionlist[self.indexList[0]][0]
            mx1 = conditionlist[self.indexList[0]][1]
            mn2 = conditionlist[self.indexList[1]][0]
            mx2 = conditionlist[self.indexList[1]][1]
            mn3 = conditionlist[self.indexList[2]][0]
            mx3 = conditionlist[self.indexList[2]][1]
            for i in range(mn1, mx1 + 1, 1):
                for j in range(mn2, mx2 + 1, 1):
                    for z in range(mn3, mx3 + 1, 1):
                        nameSet = SegmentSet([str(i),str(j), str(z)])
                        ans = self.cal(nameSet, aggrType, ans)
        return ans

class segTAggrQuery(Query):
    def __init__(self, indexFile, indexList, segTreeDict):
        super().__init__(indexFile, indexList)
        self.segTDict = segTreeDict

    def SegmentTQuery(self, conditionlist, aggrType):
        ans = 0
        conNum = len(conditionlist)
        if conNum == 1:
            ans1 = []
            mn = conditionlist[self.indexList[0]][0]
            mx = conditionlist[self.indexList[0]][1]
            seg = self.segTDict[self.indexList[0]]
            seg.decompose(seg.min,seg.max,mn,mx,ans1)
            for tup1 in ans1:
                nameSet = SegmentSet([str(tup1)])
                if nameSet in self.index:
                    ans = self.cal(nameSet, aggrType, ans)
        elif conNum == 2:
            ans1 = []
            ans2 = []
            mn1 = conditionlist[self.indexList[0]][0]
            mx1 = conditionlist[self.indexList[0]][1]
            mn2 = conditionlist[self.indexList[1]][0]
            mx2 = conditionlist[self.indexList[1]][1]
            seg1 = self.segTDict[self.indexList[0]]
            seg2 = self.segTDict[self.indexList[1]]
            seg1.decompose(seg1.min,seg1.max,mn1,mx1,ans1)
            seg2.decompose(seg2.min,seg2.max,mn2,mx2,ans2)
            for tup1 in ans1:
                for tup2 in ans2:
                    nameSet = SegmentSet([str(tup1), str(tup2)])
                    if nameSet in self.index:
                        ans = self.cal(nameSet, aggrType, ans)
        else:
            ans1 = []
            ans2 = []
            ans3 = []
            mn1 = conditionlist[self.indexList[0]][0]
            mx1 = conditionlist[self.indexList[0]][1]
            mn2 = conditionlist[self.indexList[1]][0]
            mx2 = conditionlist[self.indexList[1]][1]
            mn3 = conditionlist[self.indexList[2]][0]
            mx3 = conditionlist[self.indexList[2]][1]
            seg1 = self.segTDict[self.indexList[0]]
            seg2 = self.segTDict[self.indexList[1]]
            seg3 = self.segTDict[self.indexList[2]]
            seg1.decompose(seg1.min, seg1.max, mn1, mx1, ans1)
            seg2.decompose(seg2.min, seg2.max, mn2, mx2, ans2)
            seg3.decompose(seg3.min, seg3.max, mn3, mx3, ans3)
            for tup1 in ans1:
                for tup2 in ans2:
                    for tup3 in ans3:
                        nameSet = SegmentSet([str(tup1), str(tup2), str(tup3)])
                        ans = self.cal(nameSet, aggrType, ans)
        return ans
