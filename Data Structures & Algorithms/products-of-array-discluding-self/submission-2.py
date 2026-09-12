class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Edge conditions have to be considered. By default I would set everything to zero except the one with zero. But how would I do this in O(n) time? O(n) is a single sweep. 
        n = len(nums)
        output = [1]*n

        # 1st sweep find prefixes. 
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        #2nd Sweep uses suffixes
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output




            