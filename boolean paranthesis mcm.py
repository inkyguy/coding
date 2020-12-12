arr="T^F|F"

def solve(arr,a,b,istrue):
    ans=0
    #if a>=b:
        #return 0
    if a==b:
        if istrue=='T':
            return int(arr[a]=='T')
            #if arr[a]=='T':
                #return 1
            #else:
                #return 0
        else:
            return int(arr[b]=='F')
            #if arr[a]=='F':
                #return 1
            #else:
                #return 0
    ans=0
    for k in range(a+1,b,2):
        lt=solve(arr,a,k-1,'T')
        lf=solve(arr,a,k-1,'F')
        rt=solve(arr,k+1,b,'T')
        rf=solve(arr,k+1,b,'F')
        if arr[k]=='|':
            #print("spmething")
            if istrue=='F':
                ans+=lf*rf
            else:
                ans+=lt*rt + lf*rt + lt*rf
        if arr[k]=='&':
            if istrue=='T':
                ans+=lt*rt
            else:
                ans+=lf*rf + lf*rt + lt*rf
        if arr[k]=='^':
            if istrue=='T':
                ans+=lt*rf + lf*rt
            else:
                ans+=lt*rt + lf*rf
        #print(lt,lf,rt,rf)
    return ans
print(solve(arr,0,len(arr)-1,'T'))
