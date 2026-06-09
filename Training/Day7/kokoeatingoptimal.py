# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
# and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
# and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# [3,6,7,11],h=8
# 1 2 3 4 5 6 7 8 9 10 11
# 0 0 0 1 1 1 1 1 1  1  1
# Find first occurence of this 1

def isPossible(piles,i,h):
    hrs=0
    for p in piles:
        hrs=hrs+(p//i) if p%i==0 else hrs+(p//i)+1 
        if hrs>h:
            return False
    return True

def minEatingSpeed(piles,h):
    l=1
    r=max(piles)
    res=-1
    while l<=r:
        mid=(l+r)//2
        if isPossible(piles,mid,h):
            res=mid
            r=mid-1
        else:
            l=mid+1
    return res

print(minEatingSpeed([30,11,23,4,20],6))