class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for item in nums:
            if item in l:
                return True
            l.append(item)
        return False