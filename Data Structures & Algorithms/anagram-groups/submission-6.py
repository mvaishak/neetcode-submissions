class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        data = {w : n for n,w in enumerate('abcdefghijklmnopqrstuvwxyz')}
        for word in strs:
            counter = [0]*26
            for char in word:
                counter[data[char]] +=1
            key = ''
            for k in counter:
                key += '|' + str(k)
            if key in store:
                store[key].append(word)
            else:
                store[key] = [word]
        return list(store.values())