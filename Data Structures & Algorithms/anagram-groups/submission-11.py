class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through every string in strs
        #string -> create a "identifier" using python's ord() function
        #use this "identifier" as a key in a default dict, which maps "identifier":[list of strs]
        #return all default dict VALUES

        res = defaultdict(list)

        for string in strs:
            identifier = [0] * 26
            for character in string:
                identifier[ord(character) - ord("a")] += 1

            res[tuple(identifier)].append(string)
        
        return list(res.values())
            

        