arr=[1,3,7,3]
n=len(arr)
S=sum(arr)
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
    return dp[i]
mi=99999999
k=subset(S,arr,n)
"""
for i in range((S+1)):
    if k[i]==True:
        p=(S-(2*i)) # this iterates through whole last row of dp
        mi=min(mi,abs(p))
"""
#this iterates only half way through the last row of DP
for i in range((S+1)//2 +1):
    if k[i]==True:
        p=S-(2*i)
        mi=min(mi,p)
print(mi)
#for i in dp:
  #  print(i)