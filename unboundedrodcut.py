prc = [1 ,  5  , 8 ,  9 , 10 , 17 , 17,  20] #dataset values
le = [1 ,2 ,  3   ,4  , 5  , 6 ,  7  , 8  ]     #dataset weights
N = 8            #dataset capacity
n = len(prc) 

dp=[[-1 for i in range(N+1)]for j in range(n+1)]
def knaptd(N,le,prc,n):
    for i in range(n+1):
        for j in range(N+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif le[i-1]<=j:
                dp[i][j]=max(prc[i-1]+dp[i][j-le[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][N]
print(knaptd(N,le,prc,n))
print(dp)