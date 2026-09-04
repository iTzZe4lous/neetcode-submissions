class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        long=0
        for n in numS:
            if n-1 not in numS:
                length=1
                while n+length in numS:
                    length+=1
                long=max(length, long)
        return long