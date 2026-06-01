class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs -> group anagrams into sublists

        my_map = defaultdict(list)
        res = []

        for s in strs:
            #create a key 
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1

            my_map[tuple(key)].append(s)

        for i in my_map.values():
            res.append(i)
        return res



        