class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        codes = defaultdict(list) #counts: str[]
        res = []

        for string in strs:
            #create count key
            count = [0] * 26
            for c in string:
                #ASCII manipulation
                count[ord(c) - ord('a')] += 1
            codes[tuple(count)].append(string)#keys have to be immutable
        for l in codes.values():
            res.append(l)
        return res
        
            
                

        