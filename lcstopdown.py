a="acbcf"
b="abcdaf"
m=len(a)
n=len(b)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
#print(dp)
def lcs(a,b,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
               
            elif(a[i-1]==b[j-1]):
                dp[i][j]= 1+dp[i-1][j-1]
                
            else:
                dp[i][j]= max(dp[i][j-1],dp[i-1][j])
                
    
    return dp[m][n]
print(lcs(a,b,m,n))
for i in dp:
    print(i)
#code for printing the subsequence from here
o=''
i=len(a)
j=len(b)
while(i>0 and j>0):
    if(a[i-1]==b[j-1]):
        o+=a[i-1]
        i=i-1
        j=j-1
        #print(i,j)
    else:
        if (dp[i][j-1]>dp[i-1][j]):
            j=j-1
        else:
            i=i-1

print(o[::-1])


#printing SCSequence
o=''
i=len(a)
j=len(b)
while(i>0 and j>0):
    if(a[i-1]==b[j-1]):
        o+=a[i-1]
        i=i-1
        j=j-1
        #print(i,j)
    else:
        if (dp[i][j-1]>dp[i-1][j]):
            
            o+=b[j-1]
            j=j-1
            
        else:
            o+=a[i-1]
            i=i-1
print("Shortest common subsequence")
print(o[::-1])