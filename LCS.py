a="abcdefgh"
b="apoefbcdegh"
#dp=[[-1 for i in range(len(b)+1)]for j in range(len(a)+1)]
def lcs(a,b,m,n):
    if(n==0 or m==0):
        return 0
    if(a[m-1]==b[n-1]):
        return 1+lcs(a,b,m-1,n-1)
    else:
        return max(lcs(a,b,m,n-1),lcs(a,b,m-1,n))

print(lcs(a,b,len(a),len(b)))