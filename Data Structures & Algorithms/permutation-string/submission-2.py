class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1, s2, return true if s2 contains permutation of s2
        # look for window of len(s1) that matches char count of s1 (anagram)
        # sliding window!


        # O(26 * n) with a hashmap, size of hashmap is at most 26 characters
        # hashmap for s1 (stay the same), hashmap for s2 (chars for curr window)


        # 1. edge case
        if len(s1) > len(s2):
            return False



        # 2. Two hashmaps
        countS1 = {} # char: number of  occurrences
        countS2 = {} # char: number of occurrences


        # 3. populate countS1
        # {a: 1, b: 1, c: 1}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)

        
        # 4. Run a sliding window of fixed size len(s1) over s2. 
        # keep track of s2 (contiually update)
        # if at any point countS2 == countS1, return True
        # update the data structure to match the window you intend to check, then check
        # add -> shrink -> compare order guarantees the map is never stale relative to [l, r]

        l = 0
        for r in range(len(s2)):
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)


            while (r - l + 1) > len(s1):
                # remove character
                left_char = s2[l]
                countS2[left_char] -= 1
                # edge case: if count ever drops to 0, delete
                # del countS2[key]
                if countS2[left_char] == 0:
                    del countS2[left_char]


                # increment l
                l += 1
            
            if ((r - l + 1) == len(s1)) and countS2 == countS1:
                return True
            
        return False
        
            



            
        



        