class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for char in nums:
            counter[char] = counter.get(char,0) + 1
        rev_counter = {}
        for key,vals in counter.items():
            if vals in rev_counter:
                rev_counter[vals].append(key)
            else:
                rev_counter[vals] = [key]
        ans = []
        run = len(nums)
        while len(ans)<k:
            if run in rev_counter:
                ans += rev_counter[run]
            run -= 1
        return ans[:k]
            
