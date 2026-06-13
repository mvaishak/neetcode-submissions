class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for i in range(len(nums)):
            if nums[i] in mem:
                return True
            else:
                mem.add(nums[i])
        return False
         