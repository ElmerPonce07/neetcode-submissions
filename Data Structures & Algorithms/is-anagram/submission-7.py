class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): 
            return False

        sList = {}
        tList = {}

        for n in range(len(s)):
            sList[s[n]] = 1 + sList.get(s[n], 0)
            tList[t[n]] = 1 + tList.get(t[n], 0)

        return sList == tList 
        