class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for num, counts in count.most_common(k):
            res.append(num)
        return res

