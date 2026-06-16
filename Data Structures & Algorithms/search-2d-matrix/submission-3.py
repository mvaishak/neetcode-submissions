class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            if target <= matrix[r][n-1]:
                nums = matrix[r]
                i = 0
                j = n - 1 
                while i <= j:
                    mid = (i + j)//2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] < target:
                        i = mid +1 
                    elif nums[mid] > target:
                        j = mid-1
        return False




