class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        sol = []
        for idx in range(len(nums)):
            target = nums[idx] * -1
            i = idx+1
            j = len(nums) - 1
            while i < j:
                cur = nums[i] + nums[j]
                if cur<target:
                    i+=1
                elif cur>target:
                    j-=1
                elif cur==target:
                    cur_sol = [nums[idx],nums[i],nums[j]]
                    if cur_sol not in sol:
                        sol.append(cur_sol)
                    i+=1
                    j-=1
                else:
                    break
        return list(sol) 
                            