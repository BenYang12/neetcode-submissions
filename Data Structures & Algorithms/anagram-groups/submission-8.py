class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram -> use a hashmap
        #iterate through strs, count occurrences of each char (count will serve as key), values will be list of strs that match such counts

        count = defaultdict(list) #count of each char: [strs]
        res = []

        for string in strs:
            charCount = [0] * 26
            for char in string:
                charCount[ord(char) - ord("a")] += 1
            
            count[tuple(charCount)].append(string)

        
        for i in count.values():
            res.append(i)
        return res
        



        
        