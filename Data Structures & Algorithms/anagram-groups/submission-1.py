class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}
        for chars in strs:
            s = sorted(list(chars))
            s = ''.join(s)
            if s in mem:
                mem[s].append(chars)
            else:
                mem[s] = [chars]
        return list(mem.values())