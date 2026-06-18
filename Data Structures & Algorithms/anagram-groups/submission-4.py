class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        data = {w : n for n,w in enumerate('abcdefghijklmnopqrstuvwxyz')}
        for word in strs:
            keys = [0]*26
            for char in word:
                keys[data[char]] += 1
            key = ''
            for k in keys:
                key += '*' + str(k)
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())
            
