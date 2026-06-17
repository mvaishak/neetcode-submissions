class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles , h hours, rate of k. 
        # BINARY SEARCH !!!!

        ki = 1 
        kj = max(piles)
        k = 0
        target = kj
        while ki <= kj:
            k = (ki + kj)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/ k)
            if total_hours <= h:
                ans = k      
                kj = k - 1   
            else:
                ki = k + 1   
        return ans