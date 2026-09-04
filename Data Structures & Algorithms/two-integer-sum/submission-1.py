class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapS = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapS:
                return [mapS[diff], i]
            mapS[n] = i
