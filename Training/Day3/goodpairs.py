# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

#METHOD 1
def numIdenticalPairs(nums):
        dic={}
        count=0
        for i in (nums):
            if i in dic:
                dic[i]+=1
                count+=dic[i]
            else:
                dic[i]=0
        return count

arr=[1,2,3,1,1,3]
print(numIdenticalPairs(arr))