class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {} #char: number of occurrences


        #edge case
        if len(s1) > len(s2):
            return False
        
        for c in s1:
            countS1[c] = 1 +  countS1.get(c,0)

        #countS1 is complete
        #{a: 1, b: 1, c:1}
        #lecabee
        countS2 = {} #char: number of occurrences
        L = 0
        for R in range(len(s2)):
            countS2[s2[R]] = 1 + countS2.get(s2[R], 0)

            
            while (R - L + 1) > len(s1):
                left_char = s2[L]
                countS2[left_char] -= 1
                if countS2[left_char] == 0:
                    del countS2[left_char]
                L += 1
                

            if (R - L + 1 == len(s1)) and countS2 == countS1:
                return True 
        return False
                
            
        
    

        

        

        
        
        