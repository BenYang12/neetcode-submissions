class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, prevHeight, visit):
            #base case
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visit or prevHeight > heights[r][c]:
                return
            
            visit.add((r,c))

            #call dfs on all 4-directionally adjacent positions
            #mark all nodes that can reach the pacific or atlantic ocean depending on which set we pass in
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
        

        #rows
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)
        #cols
        for r in range(rows):
            dfs(r, 0,heights[r][0], pac)
            dfs(r, cols - 1,heights[r][cols - 1], atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


         








        

        