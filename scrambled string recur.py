a="sohail"
b="lhsoai"

def solve(a,b):
    n=len(a)
    if len(a)!=len(b):
        return False
    if not n:
        return True
    if sorted(a)!=sorted(b):
        return False
    if a==b:
        return True
    #flag=False
    for i in range(1,n):
        c1=solve(a[:i],b[:i]) and solve(a[i:],b[i:])
        c2=solve(a[-i:],b[:i]) and solve(a[:-i],b[i:])
        if c1 or c2:
            return True
        

    return False

print(solve(a,b))