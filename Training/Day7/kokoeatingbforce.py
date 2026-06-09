# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
# and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
# and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

#METHOD 1 - BRUTE FORCE     ->      But requires lot of time in several cases
def minEatingSpeed(piles, h):
    if h<len(piles):
        return -1
    elif h==len(piles):
        return max(piles)
    for i in range(1,max(piles)+1):
        hrs=0
        for p in piles:
            hrs=hrs+(p//i) if p%i==0 else hrs+(p//i)+1 
            if hrs>h:
                break
        if hrs<=h:
            return i
        
print(minEatingSpeed([30,11,23,4,20],6))
