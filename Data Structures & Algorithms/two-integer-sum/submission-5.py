class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,num in enumerate(nums):
            t = target - num
            if t in d:
                return [d[t],index]
            else:
                d[num] = index
           