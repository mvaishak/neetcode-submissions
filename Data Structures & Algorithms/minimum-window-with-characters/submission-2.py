class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        t_counter = {}
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        required = len(t_counter)
        window_counts = {}
        formed = 0
        l = 0
        min_len = len(s) + 1
        start_idx = 0

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_counter and window_counts[char] == t_counter[char]:
                formed += 1

            while l <= r and formed == required:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    start_idx = l

                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in t_counter and window_counts[left_char] < t_counter[left_char]:
                    formed -= 1
                l += 1

        return "" if min_len > len(s) else s[start_idx : start_idx + min_len]
