a="abcsae"
b="abcecdce"
m=len(a)
n=len(b)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
print(dp)
def lcs(a,b,m,n):
    x=0
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
               
            elif(a[i-1]==b[j-1]):
                dp[i][j]= 1+dp[i-1][j-1]
                
            else:
                dp[i][j]= 0
            
            x=max(x,dp[i][j])
            
    return x
print(lcs(a,b,m,n))
print(dp)