class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        picked=[False]*len(nums)

        def dfs(cur, picked):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if not picked[i]:
                    cur.append(nums[i])
                    picked[i]=True
                    dfs(cur, picked)
                    cur.pop()
                    picked[i]=False
        dfs(cur, picked)
        return res
