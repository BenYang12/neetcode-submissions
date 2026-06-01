class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}#char: number of occurences

        for c in s:
            s_dict[c] = 1 + s_dict.get(c,0)

        for c in t:
            t_dict[c] = 1 + t_dict.get(c,0)

        return s_dict == t_dict

        