class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevpath = [0] * n

        for r in range(m - 1, -1, -1):
            curpath = [0] * n

            curpath[n - 1] = 1

            for c in range(n - 2, -1, -1):
                curpath[c] = curpath[c+1] + prevpath[c]
            
            prevpath = curpath
        
        return prevpath[0]
        