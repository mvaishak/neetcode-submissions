class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the size of the sliding window will be the size of s1 so its a static window size 
        if len(s1) > len(s2): #first edge case to come to mind
            return False
        hashmap = {}
        for c in s1:
            hashmap[c] = hashmap.get(c, 0) + 1
        dashmap = {}
        k = len(s1)
        i = 0 # left pointer

        for j in range(len(s2)): #right pointer
            
            c = s2[j]
            dashmap[c] = dashmap.get(c, 0) + 1

            if (j- i + 1) == k:
                if hashmap == dashmap:
                    return True
                out = s2[i]
                dashmap[out] -= 1
                if dashmap[out] == 0:
                    del dashmap[out]
                i += 1
        return False
