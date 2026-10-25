class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def dfs(i, subset):
            if i==len(nums) and subset in res:
                return
            elif i==len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
        dfs(0, subset)
        return res