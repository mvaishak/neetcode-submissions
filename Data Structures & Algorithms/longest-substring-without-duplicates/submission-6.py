class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        i = 0
        max_len = 0
        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1

            hashset.add(s[j])
            max_len = max(len(hashset),max_len)
        return max_len


            
