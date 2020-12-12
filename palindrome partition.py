import sys
arr="nitik"
dp=[[-1 for i in range(len(arr))] for j in range(len(arr))]
def ispal(arr,a,b):
    k= arr[a:b+1]
    print(k)
    return k==k[::-1]
def solve(arr,a,b):
    mi=sys.maxsize
    if a>=b:
        return 0
    if ispal(arr,a,b):
        return 0
    if dp[a][b]!=-1:
      return dp[a][b]
    for k in range(a,b):
        temp=solve(arr,a,k)+solve(arr,k+1,b)+1
       # print(arr[a-1],arr[k],arr[b])
        if temp<mi:
            mi=temp
    dp[a][b]=mi

    return dp[a][b]
print(solve(arr,0,len(arr)-1))

for i in dp:
    print(i)