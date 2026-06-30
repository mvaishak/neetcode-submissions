class TimeMap:

    def __init__(self):
        # Maps key to a list of (timestamp, value) tuples
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]
        i = 0
        j = len(values) - 1
        res = ""

        # Correct Binary Search
        while i <= j:
            m = (i + j) // 2
            cur_time = values[m][0]
            
            if cur_time == timestamp:
                return values[m][1]
            elif cur_time < timestamp:
                res = values[m][1]  # Valid candidate, but check if there's a closer one
                i = m + 1
            else:
                j = m - 1
                
        return res