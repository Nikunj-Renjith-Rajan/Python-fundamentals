#Write a code for sliding window protocol with largest sub array sum for sub array size k
arr=[9,8,6,5,7,3,2,9,4,7,2,6,1,9]
ws=4            #windowsize
m=0
tempmax=0
for i in range(0,ws):
    tempmax+=arr[i]
m=tempmax
for i in range(1,len(arr)-ws):
    prevsum=tempmax
    tempmax=prevsum-arr[i-1]+arr[i+ws-1]
    if tempmax>m:
        m=tempmax
print(m)
