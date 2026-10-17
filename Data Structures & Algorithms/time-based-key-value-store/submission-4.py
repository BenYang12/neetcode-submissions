class TimeMap:
    def __init__(self):
        self.store = {} # key: list of [val, timestamp]
    
    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = [] # create empty list
        
        # append to list
        self.store[key].append([value, timestamp])
    
    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [] )
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    


