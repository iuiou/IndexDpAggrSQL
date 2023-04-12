from model import attr
# Temporarily ignore float value,
# if value type is float, it can be discretized
class SegmentTree:
    def __init__(self, attri: attr):
        self.min = 1
        self.max = len(attri.dcarray)
        self.seglist = list()
        self.build(self.min, self.max)
        self.raw_data = attri.dcarray

    def build(self, L, R):
        self.seglist.append((L,R))
        if L == R:
            return
        mid = (L + R) // 2
        self.build(L, mid)
        self.build(mid+1, R)

    def decompose(self, L, R, l, r, ans):
        if l <= self.raw_data[L] and r >= self.raw_data[R]:
            ans.append((L, R))
            return
        mid = (L + R) // 2
        if mid >= l:
            self.decompose(L, mid, l, r, ans)
        if r > mid:
            self.decompose(mid+1, R, l, r, ans)

    def show(self):
        print(self.seglist)



