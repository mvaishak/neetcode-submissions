class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = 0 
        i, j = [0,0]
        for index in range(len(nums)):
            num = nums[index]
            pot_ans = target - num
            if pot_ans in nums[index+1:]:
                ans = pot_ans
                i = index
                break
        for index in range(len(nums)):
            if (nums[index] == ans) and index!=i:
                j = index
                break
        return [i,j]
        