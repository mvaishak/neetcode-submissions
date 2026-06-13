class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in mem:
                return [mem[res],i]
            else:
                mem[nums[i]] = i
        return 0
        