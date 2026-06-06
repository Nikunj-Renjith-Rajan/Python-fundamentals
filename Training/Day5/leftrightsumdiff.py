# You are given a 0-indexed integer array nums of size n. Define two arrays leftSum and rightSum where:
# leftSum[i] is the sum of elements to the left of the index i in the array nums.
# If there is no such element, leftSum[i] = 0. rightSum[i] is the sum of elements 
# to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

def leftRightDifference(nums):
        ans=[]
        s=sum(nums)
        lsum=0
        rsum=s
        for i in range(len(nums)):
            if i!=0:
                lsum+=nums[i-1]
            rsum-=nums[i]
            ans.append(abs(lsum-rsum))
        return ans

print(leftRightDifference([10,4,8,3]))