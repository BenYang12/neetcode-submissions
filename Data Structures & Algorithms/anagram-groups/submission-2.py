class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #id:list

        for s in strs:
            id = [0] * 26

            for c in s:
                id[ord(c) - ord('a')] +=1 

            res[tuple(id)].append(s) 
            
        return list(res.values())

        


        
        