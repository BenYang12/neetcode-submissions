class TimeMap:
    # store multiple values for the same key at different time stamps
    # retrieve the key's value at a certain timestamp
    # timestamps are strictly increasing

    def __init__(self):
        self.store = {} # key -> list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] # create emtpy list
        
        # append to list
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) # [ ["happy":1], ...]

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
        
