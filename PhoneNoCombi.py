#BACKTRACKING
letters= {2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz"}
l=''
ans=[]
def noCombi(digits):
    backtrack(0,l,digits)

def backtrack(index,l,digits):
    if(len(l)==len(digits)):
        ans.append(l)
        return
    possible =list(letters[int(digits[index])])
    for char in possible:
        #do
        l+=(char)
        #recurse
        backtrack(index+1,l,digits)
        #undo
        l=l[:-1]
noCombi("234")
print(ans,len(ans))