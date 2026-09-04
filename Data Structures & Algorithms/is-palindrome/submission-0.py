class Solution:
    def isPalindrome(self, s: str) -> bool:
        eStr=""
        for c in s:
            if c.isalnum():
                eStr+=c.lower()
        return eStr == eStr[::-1]
