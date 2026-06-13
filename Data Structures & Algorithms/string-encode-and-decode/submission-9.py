class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            term = s[j + 1 : j + 1 + length]
            decoded.append(term)
            i = j + 1 + length
            
        return decoded
        
