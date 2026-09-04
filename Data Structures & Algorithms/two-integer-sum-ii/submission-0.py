class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp ={}
        for i in range(len(numbers)):
            tmp=target-numbers[i]
            if tmp in mp:
                return [mp[tmp]+1, i+1]
            mp[numbers[i]]=i
        return []
