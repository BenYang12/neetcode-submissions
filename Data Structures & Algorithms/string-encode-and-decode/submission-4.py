class Solution:

    def encode(self, strs: List[str]) -> str:
        #list of strs -> singular str
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        #str -> list of strs
        res = []
        i = 0 

        while i < len(s):
            #find the delimiter first!
            j = i
            while s[j] != "#":
                j  += 1
            length = int(s[i:j])
            res.append(s[j+1:j + 1 + length])

            #update pointer i
            i = j + 1 + length
        return res
            


