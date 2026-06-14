class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        sol = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
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
                    sol.append(cur_sol)
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i+=1
                    j-=1
                else:
                    break
        return list(sol) 
                            