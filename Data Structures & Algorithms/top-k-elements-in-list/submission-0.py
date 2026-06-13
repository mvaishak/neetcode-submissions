from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = defaultdict(int)
        for num in nums:
            A[num] +=1
        sorted_A_asc = [k for k, v in sorted(A.items(), key=lambda item: item[1])]
        sorted_A_asc.reverse()
        return sorted_A_asc[:k]
