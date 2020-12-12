import sys

arr=[2,3,5,2,4,3]
def solve(arr,i,j):
    mi=sys.maxsize
    if i>=j:
        return 0
    for k in range(i,j):
        temp=(solve(arr,i,k)+solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
        #print(temp)
        if temp<mi:
            mi=temp
    return mi
print(solve(arr,1,len(arr)-1))