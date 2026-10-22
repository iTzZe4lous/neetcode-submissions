class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        nums.sort()

        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if total+nums[j]>target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total+nums[j])
                cur.pop()
        dfs(0, cur, 0)
        return res