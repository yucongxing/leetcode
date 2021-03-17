class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # method one: DFS

        #def dfs(s: str, t:str, ss: int, ts: int) -> int:
            #n = len(s)
            #m = len(t)
            #if n-ss < m-ts:
                #return 0
            #if ss >= n or ts >= m:
                #return 0
            #curnum = 0
            #if ts == m - 1:
                #for i in range(ss, n):
                    #if s[i] == t[ts]:
                        #curnum += 1
            #else:
                #for i in range(ss, n):
                    #if s[i] == t[ts]:
                        #curnum += dfs(s, t, i+1, ts+1)
            #return curnum    
        #return dfs(s, t, 0, 0)

        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            dp[m][i] = 0
        for i in range(m+1):
            dp[i][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct('babgbag', 'bag'))
    print(s.numDistinct('rabbbit', 'rabbit'))
    print(s.numDistinct("babeceeacaadababaceacbcbdaeddedbbccddbdadaedbbccdbcaebecdacdedaaccaabecbbdcdeececbcbebacbebdcbdbaebbabadbcdbbacddebcabaecdccecdbdcaddacecacada","adebd"))
