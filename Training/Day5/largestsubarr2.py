#Find the length of largest sub array with sum <= k             
#METHOD 2- 2 POINTER + GREEDY
arr=[7,6,8,5,4,1,5,1,6,6,8,9,5,6]
k=28
maxc=0
s=0
l=r=0
st=0
while r<len(arr):
    s+=arr[r]
    if s<=k:
        if r-l+1 > maxc:
            maxc=r-l+1
            st=l
        r+=1
    else:
        s=s-arr[l]
        l+=1
        r+=1
        
print(maxc)
for i in range(st,st+maxc):
    print(arr[i],end=" ")