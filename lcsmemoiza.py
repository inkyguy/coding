a="abcdefgh"
b="apoefbcdegh"
m=len(a)
n=len(b)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
print(dp)
def lcs(a,b,m,n):
    
        if(n==0 or m==0):
            dp[m][n]=0
            return dp[m][n]
        if dp[m][n]!=-1:
            return dp[m][n]
        elif(a[m-1]==b[n-1]):
            dp[m][n]= 1+lcs(a,b,m-1,n-1)
            return dp[m][n]
        else:
            dp[m][n]= max(lcs(a,b,m,n-1),lcs(a,b,m-1,n))
            return dp[m][n]
    

print(lcs(a,b,m,n))
print(dp)