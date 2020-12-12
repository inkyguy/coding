arr = [1,2,3]     #dataset weights
S = 5   #dataset capacity
n = len(arr)
dp=[[0 for i in range(S+1)]for j in range(n+1)]
for j in range(S+1):
    dp[0][j]=0
for i in range(n+1):
    dp[i][0]=1
    
#for i in dp:
  #  print(i)
def subset(S,arr,n):
    for i in range(1,n+1):
        for j in range(1,S+1):
            if arr[i-1]<=j:
                dp[i][j]=(dp[i-1][j-arr[i-1]] + dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    #print(dp)
    return dp[n][S]

    
print(subset(S,arr,n))
#print(dp)
# for i in dp:
   # print(i)