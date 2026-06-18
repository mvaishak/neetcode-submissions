class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
        print(d)
        val_dict = {}
        for key , v in d.items():
            if v in val_dict:
                val_dict[v].append(key)
            else:
                val_dict[v] = [key]
        ans = []
        print(val_dict)
        print(k)
        for i in range(len(nums),-1,-1):
            if i in val_dict:
                ans += val_dict[i]
                if len(ans) >= k:
                    print(ans)
                    return ans[:k]
        return ans[:k]