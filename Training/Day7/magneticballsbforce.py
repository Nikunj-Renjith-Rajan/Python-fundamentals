# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put 
# in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and 
# needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

#METHOD 2 -> BINARY SEARCH METHOD
def maxDistance(position, m):
        pos=sorted(position)
        res=0
        for i in range(1,pos[-1]-pos[0]+1):
                j=1
                cnt=1
                prev=0
                while j<len(pos):
                        if pos[j]-pos[prev]>=i:
                                prev=j
                                cnt+=1
                        j+=1 
                        if cnt==m:
                                res=i
                                break  
        return res    

                       
print(maxDistance([1,2,3,4,7],3))