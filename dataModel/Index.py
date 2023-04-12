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
    def __init__(self, raw_data, IndexKeySet, aggrType):
        self.index = dict()



