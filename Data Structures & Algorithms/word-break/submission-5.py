class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #string s, wordDict -> true if s can be segmented into a space-    separated sequence of dictionary words

        #allowed to reuse words in dictionary an unlimited number of times


        # s = "neetcode True", wordDict = ["neet", "code"]
        # bottom up DP

        dp = [False] * len(s)
        dp.append(True) #base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(dp) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
                    

        return dp[0]


        




        