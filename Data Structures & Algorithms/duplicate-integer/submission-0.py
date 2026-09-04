class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenVals = set()
        for num in nums:
            if num in seenVals:
                return True
            seenVals.add(num)
        return False