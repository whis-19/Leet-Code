class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        myDict = {}
        for i in s1:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        for i in s2:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        mySet = set()
        for i in myDict:
            if myDict[i] == 1:
                mySet.add(i)
        return list(mySet)
        