class TimeMap:
    # time-based kv store -> multiple values for same key at diff time stamps
    # retrieve the key's value at a certain timestamp
    # strictly increasing -> hints toward binary search!

    def __init__(self):
        self.store = {} # key: list of [value, timestamp] 

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # handle edge cases

        if key not in self.store:
            self.store[key] = [] # create empty list


        # append to list
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # returns val s.t. set was called previously, 
        # with timestamp_prev <= timestamp
        res = ""
        values = self.store.get(key, []) # [["happy", 1], ...]
        # timestamps: 1, 2, 3, 4, 5

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                # go right
                res = values[m][0]
                l = m + 1
            else:
                # go left
                r = m - 1
            
        return res


        
        
