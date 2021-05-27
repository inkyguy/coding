N = 50000
k=[]
for i in range(N+1):
    k.append(i)
#print(len(k))
while(len(k)>2):
    for i in range(len(k)-1,-1,-1):
        if(i%2!=0):
            k.remove(k[i])
            #print(k,i)     16     
print(k[1])