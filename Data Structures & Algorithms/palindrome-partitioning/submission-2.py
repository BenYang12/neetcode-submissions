class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] #store all the partitions we create
        part = [] #current partition

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l,r = l + 1, r - 1
            return True

        def dfs(i):
            #pass in index

            #base case
            if i >= len(s):
                res.append(part.copy())
                return

            #generate every single possible substring. If substring is a palindrome, recursively continue dfs. If not palindrome, then we just skip it
            for j in range(i, len(s)):
                #for every possible substring
                if isPali(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
        