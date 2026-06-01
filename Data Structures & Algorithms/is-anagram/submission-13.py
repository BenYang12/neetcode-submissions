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



        