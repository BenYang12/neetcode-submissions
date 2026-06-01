class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use two hashmaps -> compare hashmaps at end
        if len(s) != len(t):
            return False

        
        #two hashmaps
        #char: number of occurrences
        countS = {} 
        countT = {}

        for c in s:
            countS[c] = 1 + countS.get(c,0)

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        return countS == countT

        #TC: O(n + m), where n is the length of string s and m is the length of string t. 
        #SC: O (1), we have at most 26 different characters



        