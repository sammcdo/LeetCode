class SmallestInfiniteSet:

    def __init__(self):
        self.removed = []
        

    def popSmallest(self) -> int:
        self.removed.sort()
        if len(self.removed) == 0:
            self.removed.append(1)
            return 1
        elif len(self.removed) == 1:
            num = self.removed[0]
            if num == 1:
                self.removed.append(2)
                return 2
            else:
                self.removed.append(1)
                return 1
        else:
            num = float("inf")
            a = self.removed.copy()
            a.insert(0,0)
            for i in range(1, len(a)):
                if a[i-1]+1 != a[i]:
                    if a[i-1]+1 < num:
                        num = a[i-1]+1
            if a[-1]+1 < num:
                num = a[-1]+1
            
            self.removed.append(num)
            return num

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)