class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        z = 0
        for mem in nums:
            if mem != 0:
                tot *= mem
            else:
                z+=1

        if z==1:
            return [0 if k!=0 else tot for k in nums]
        elif z>1:
            return [0]*len(nums)
        else:
            return [tot//k for k in nums]