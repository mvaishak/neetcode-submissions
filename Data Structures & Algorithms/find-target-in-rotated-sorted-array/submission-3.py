class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left: int, right: int) -> int:
            l, r = left, right
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        n = len(nums)
        if n == 0:
            return -1
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        pivot = l  
        if pivot == 0:
            return binary_search(0, n - 1)
        if nums[0] <= target <= nums[pivot - 1]:
            return binary_search(0, pivot - 1)
        else:
            return binary_search(pivot, n - 1)



        