class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data_s = {}
        data_t = {}
        for a in s:
            data_s[a] = data_s.get(a,0) + 1
        for a in t:
            data_t[a] = data_t.get(a,0) + 1
        if data_s == data_t:
            return True
        else:
            return False