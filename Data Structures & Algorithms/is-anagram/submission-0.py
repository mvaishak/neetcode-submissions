class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = sorted(list(s))
        c2 = sorted(list(t))
        if c1==c2:
            print(c1)
            print(c2)
            return True
        else:
            return False
        