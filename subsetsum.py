#similar to knapsack, tells yes or no whether a subset of the given array can form the sum or not 
arr = [2,3,5]     #dataset weights
S = 10   #dataset capacity
n = len(arr)
dp=[[False for i in range(S+1)]for j in range(n+1)]
for i in range(n+1):
        dp[i][0]=True

def subset(S,arr,n):
    for i in range(1,n+1):
        for j in range(1,S+1):
            if arr[i-1]<=j:
                dp[i][j]=(dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    #print(dp)
    return dp[i][j]

    
print(subset(S,arr,n))
#for i in dp:
 #   print(i)