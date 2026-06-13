class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for char in strs:
            temp = list(char)
            temp.sort()
            temp = ''.join(temp)
            if temp in A:
                A[temp].append(char)
            else:
                A[temp] = [char]
        ans = []
        for keys, values in A.items():
            ans.append(values)
        return ans

        