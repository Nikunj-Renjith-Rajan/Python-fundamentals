#Find the length of largest sub array with sum <= k             
#METHOD 1-BRUTE FORCE + GREEDY
arr=[7,6,8,5,4,1,5,1,6,6,8,9,5,6]
k=28
maxc=0
for i in range(len(arr)):
    s=0
    cnt=0
    for j in range(i,len(arr)):
        s=s+arr[j]
        if s<=k:
            cnt+=1
            maxc=max(maxc,cnt)
        else:
            break
print(maxc)
