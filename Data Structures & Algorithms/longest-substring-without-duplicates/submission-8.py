class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        count = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c,0) + 1
            while count[c] > 1 :
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            max_len = max(max_len,r - l + 1)
        return max_len