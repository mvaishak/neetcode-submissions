class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_len = 0
        max_freq = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c,0) + 1
            max_freq = max(max_freq,count[c])
            print(c,max_freq)
            while (r-l+1) - max_freq > k:
                print('entered')
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            print('Max len :', max_len)
        
        return max_len