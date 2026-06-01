class Solution:

    #list -> single string
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res
         

    #single string -> list
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i #j starts out at 0
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) #start of word after #: length of word
            i = j + 1 + length #beginning of next string
        return res

        
