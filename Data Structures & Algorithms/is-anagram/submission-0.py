class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sString, tString = {}, {}

        for i in range(len(s)):
            sString[s[i]] = sString.get(s[i], 0) + 1
            tString[t[i]] = tString.get(t[i], 0) + 1
        return sString == tString