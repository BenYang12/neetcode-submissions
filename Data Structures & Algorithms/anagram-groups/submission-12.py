class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs -> groupo all anagrams together into sublists
        # 1. iterate through strs
        # 2. count chars -> create unique key for every single string
        # 3. add this key to a hashmap, then return entire thing as a list

        res = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c) - ord("a")] += 1 
            
            res[tuple(key)].append(string)

        
        return list(res.values())


            
        


            

            

            



        
        
        