class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #char_count: []

        for s in strs:
            count = [0] * 26 #a-z, this is ekey

            #iterate through every character in string -> count char
            for c in s:
                count[ord(c) - ord("a")] += 1 #subtract ascii of a (a - a = 0)
            
            #add this count into our dict
            #What if this count doesn't exist yet
            res[tuple(count)].append(s)
        return list(res.values())
        



            





        