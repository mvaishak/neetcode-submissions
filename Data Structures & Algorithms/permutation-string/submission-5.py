class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Because we are looking for a substring of a particular legth, its a fixed window. In the case of abc, move the window and check count of elements in it, if the counts match, we good bruh
        window_size = len(s1)
        l=0
        r=l+window_size-1
        s1_count = {}
        s2_count = {}
        for e in s1:
            s1_count[e] = s1_count.get(e,0) + 1
        for e in s2[:window_size]:
            s2_count[e] = s2_count.get(e,0) + 1

        while r<len(s2):
            if s1_count == s2_count:
                return True
        
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            l+=1
            r+=1
            if r < len(s2):
                s2_count[s2[r]] = s2_count.get(s2[r],0) + 1
                
        return s1_count == s2_count

