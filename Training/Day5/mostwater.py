# You are given an integer array height of length n. There are n vertical lines drawn such that the two 
# endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.


#METHOD 1 - BRUTE FORCE (O(n*n))
def maxArea1(height):
        maxvol=-0
        for i in range(len(height)):
            length=1
            for j in range(i+1,len(height)):
                maxvol=max(maxvol,length*min(height[i],height[j]))
                length+=1
        return maxvol

#METHOD 2 - 2 POINTER
def maxArea2(height):
        maxvol=-0
        left=0
        right=len(height)-1
        while left<right:
            length=right-left
            maxvol=max(maxvol,length*(min(height[left],height[right])))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxvol

print(maxArea1([1,8,6,2,5,4,8,3,7]))
print(maxArea2([1,8,6,2,5,4,8,3,7]))