class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWord = ''
        for s in strs:
            encodedWord += str(len(s)) + '#' + s
        return encodedWord

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            stringCount = int(s[i:j])
            i = j+1
            j = i + stringCount
            res.append(s[i:j])
            i = j
        return res
