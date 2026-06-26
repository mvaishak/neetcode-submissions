class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        map2 = {}
        for c in s1:
            map1[c] = map1.get(c,0) + 1
        
        l = 0 
        for r in range(len(s2)):
            c = s2[r]
            map2[c] = map2.get(c,0) + 1
            if (r-l+1) == len(s1):
                if map2 == map1:
                    return True
                else:
                    map2[s2[l]] -=1
                    if map2[s2[l]] == 0:
                        del map2[s2[l]]
                    l += 1
                
        return False