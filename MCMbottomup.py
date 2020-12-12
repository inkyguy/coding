import sys
arr=[30,35,15,5,10,20,25]
dp=[[-1 for i in range(len(arr))] for j in range(len(arr))]

def solve(arr,a,b):
    mi=sys.maxsize
    if a>=b:
        return 0
    if dp[a][b]!=-1:
      return dp[a][b]
    for k in range(a,b):
        temp=solve(arr,a,k)+solve(arr,k+1,b)+(arr[a-1]*arr[k]*arr[b])
       # print(arr[a-1],arr[k],arr[b])
        if temp<mi:
            mi=temp
    dp[a][b]=mi

    return dp[a][b]
print(solve(arr,1,len(arr)-1))

for i in dp:
    print(i)