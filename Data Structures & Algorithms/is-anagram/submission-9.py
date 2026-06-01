class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {} #char: count
        tdict = {} #char: count

        for char in s:
            sdict[char] = 1 + sdict.get(char, 0)
        for char in t:
            tdict[char] = 1 + tdict.get(char,0)
        
        return sdict == tdict
            
           







    
        