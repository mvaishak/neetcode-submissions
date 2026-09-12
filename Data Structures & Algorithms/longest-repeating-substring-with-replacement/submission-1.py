class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_len = 0
        most_freq = 0

        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char,0) + 1
            most_freq = max(count[char],most_freq)
            while (r - l + 1) - most_freq > k :
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
