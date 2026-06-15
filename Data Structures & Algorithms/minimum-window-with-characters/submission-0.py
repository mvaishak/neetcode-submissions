class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #This is a dynamic window
        # Keep increasing right then reduce left when condition gets violated
        # Once every character in t is in s, reduce s and see if the len reduces. Once violated again, continue to increase.
        if not t or not s:
            return ''
            
        hashmap = {}
        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1

        dashmap = {}
        have = 0
        need = len(hashmap)
        
        min_len = math.inf
        output = {math.inf: ''}
        l = 0


        for r in range(len(s)):
            c = s[r]
            if c in hashmap:
                dashmap[c] = dashmap.get(c,0) + 1
                if dashmap[c] == hashmap[c]: # We have collected enough chars of c
                    have += 1
            while have == need :
                # Now I can reduce the l to see how small I can get the length to be 
                current_len = r - l + 1
                if current_len < min_len : #Update the smallest substring
                    min_len = current_len 
                    output[min_len] = s[l:r+1]
                
                out = s[l]
                if out in hashmap:
                    dashmap[out] -= 1
                    if dashmap[out] < hashmap[out]:
                        have -= 1
                l += 1
            
        return output[min_len]