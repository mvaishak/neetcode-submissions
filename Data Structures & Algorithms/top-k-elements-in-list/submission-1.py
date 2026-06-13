class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        for char in nums:
            if char in mem:
                mem[char] +=1
            else:
                mem[char] = 1
        
        return [k for k,v in sorted(mem.items(), key= lambda item : item[1])][-k:]