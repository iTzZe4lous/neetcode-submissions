class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check=set()
        for i in nums:
            if i in check:
                return i
            check.add(i)
        return -1