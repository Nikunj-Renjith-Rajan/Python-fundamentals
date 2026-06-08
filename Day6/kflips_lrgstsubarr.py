# Find the longest sub array with consecutive ones with at most k flips/
# Flip means flipping a 0 to 1
arr=[0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1]
k=4
z=0
l=r=0
maxlen=0
while r<len(arr):
    if arr[r]==0:
        z+=1
    r+=1
    while z>k:
        if arr[l]==0:
            z-=1
        l+=1
    maxlen=max(maxlen,r-l)
print(maxlen)
    