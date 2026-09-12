class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for n,w in enumerate(nums):
            print(w,n)
            print(d)
            cur_target = target - w
            if cur_target in d:
                return [d[cur_target][0],n]
            if w in d:
                d[w].append(n)
            else:
                d[w] = [n]