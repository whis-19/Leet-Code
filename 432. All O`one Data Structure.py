class AllOne:
    def __init__(self):
        self.myDict = {}

    def inc(self, key: str) -> None:
        if key in self.myDict:
            self.myDict[key] += 1
        else:
            self.myDict[key] = 1

    def dec(self, key: str) -> None:
        if key in self.myDict:
            self.myDict[key] -= 1
            if self.myDict[key] == 0:
                del self.myDict[key]
        

    def getMaxKey(self) -> str:
        if len(self.myDict) == 0:
            return ""
        else:
            return max(self.myDict, key=self.myDict.get)
        

    def getMinKey(self) -> str:
        if len(self.myDict) == 0:
            return ""
        else:
            return min(self.myDict, key=self.myDict.get)
        


