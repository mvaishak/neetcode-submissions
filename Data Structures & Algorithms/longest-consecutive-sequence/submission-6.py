class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collect = set(nums)
        max_len = 0
        length = 0
        for num in nums:
            if num-1 not in collect:
                length = 0
                while (num +length) in collect:
                    length += 1
                max_len = max(max_len,length)
        return max_len
