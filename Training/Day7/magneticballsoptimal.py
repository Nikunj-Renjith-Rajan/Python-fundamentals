# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put 
# in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and 
# needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

#For the input 1 2 4 8 9

# 1 2 3 4 5 6 7 8
# 1 1 1 0 0 0 0 0
# So we have to find this last occuring 1

#METHOD 2 -> OPTIMAL METHOD
def isPossible(pos,m,mid):
        j=1
        cnt=1
        prev=0
        while j<len(pos):
                if pos[j]-pos[prev]>=mid:
                        prev=j
                        cnt+=1
                j+=1 
                if cnt==m:
                        return True
        return False
                         
def maxDistance(position, m):
        pos=sorted(position)
        if m==2:
                return pos[-1]-pos[0]
        l=1
        r=pos[-1]
        res=-1
        while l<=r:
                mid=(l+r)//2
                if isPossible(pos,m,mid):
                        res=mid
                        l=mid+1
                else:
                        r=mid-1
        return res
                       
print(maxDistance([1,2,4,8,9],3))
print(maxDistance([79,74,57,22],4))