
# Temporarily ignore float value,
# if value type is float, it can be discretized
class SegmentTree:
    def __init__(self, attri):
        self.min = 1
        self.max = len(attri.dcarray) - 1
        self.seglist = list()
        self.build(self.min, self.max)
        self.dcarray = attri.dcarray

    def find(self, L, R, pos, ans):
        ans.append((L,R))
        if L == R:
            return
        mid = (L + R) // 2
        if pos <= self.dcarray[mid]:
            self.find(L, mid, pos, ans)
        else:
            self.find(mid+1, R, pos, ans)

    def decompose(self, L, R, l, r, ans):
        if l <= self.dcarray[L] and r >= self.dcarray[R]:
            ans.append((L, R))
            return
        mid = (L + R) // 2
        if mid >= l:
            self.decompose(L, mid, l, r, ans)
        if r > mid:
            self.decompose(mid+1, R, l, r, ans)

    # def show(self):
    #     print(self.seglist)



