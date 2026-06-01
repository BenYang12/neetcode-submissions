class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        
        countsS = {} #char: number of occurrences
        countsT = {} #char: number of occurrences

        for c in s:
            countsS[c] = 1 + countsS.get(c,0) #c = char is a key

        for c in t:
            countsT[c] = 1 + countsT.get(c,0)

        return countsS == countsT

        #O(n + m)
        #O(n + m)
        

        