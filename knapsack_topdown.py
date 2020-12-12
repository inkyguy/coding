val = [10,15,40] #dataset values
wt = [1,2,3]     #dataset weights
W = 6            #dataset capacity
n = len(val) 

dp=[[-1 for i in range(W+1)]for j in range(n+1)]
def knaptd(W,wt,val,n):
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
                dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][W]
print(knaptd(W,wt,val,n))
for i in dp:
    print(i)
