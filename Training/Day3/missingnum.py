# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
# 2 is the missing number in the range since it does not appear in nums.

def missingNumber(nums):
        s1=(len(nums)*(len(nums)+1))//2
        s2=sum(nums)
        return s1-s2

print(missingNumber([1,0,3]))