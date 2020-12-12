val = [10,15,40] 
wt = [1,2,3] 
W = 6
n = len(val)
dp=[[-1 for i in range(W+1)]for j in range(n+1)]

def knaprec(W, wt, val, n):
    if dp[n][W]!=-1:
        return dp[n][W]
    elif n==0 or W==0:
        return 0
    
    elif wt[n-1]<=W:
        dp[n][W]= max((val[n-1]+knaprec(W-wt[n-1], wt, val, n-1)), knaprec(W, wt, val, n-1))
        return dp[n][W]
    else:
        dp[n][W]= knaprec(W, wt, val, n-1)
        return dp[n][W]

print(knaprec(W, wt, val, n)) 
#for i in dp:
    #print(i)
