class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s)!=len(t)):
            return False
        
        tAnagram = defaultdict(list)
        sAnagram = defaultdict(list)

        for i in range(len(s)):
            tAnagram[t[i]] = 1 + tAnagram.get(t[i],0)
            sAnagram[s[i]] = 1 + sAnagram.get(s[i],0)

        return tAnagram == sAnagram

        