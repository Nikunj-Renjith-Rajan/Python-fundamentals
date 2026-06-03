#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#METHOD 1 : BRUTE FORCE  -> O(n*n)
def twoSum1(nums, target):
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

#METHOD 2 : 2 POINTER   -> O(nlogn)
def twoSum2(nums, target):
        nums.sort()
        i=0
        j=len(nums)-1
        while i<len(nums) and j>0:
            if target<nums[i]+nums[j]:
                 j-=1
            elif target>nums[i]+nums[j]:
                 i+=1
            else:
                 return [i,j]
            
#METHOD 3 : USING DICTIONARY (HASHING)       -> Lesser time complexity    (Searching in set and dictionary requires lesser time complexity)
def twoSum3(nums, target):
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        for i in range(len(nums)):
             if target-nums[i] in dic and dic[target-nums[i]]!=i:
                  return [i,dic[target-nums[i]]]
             
# #METHOD 4 : USING DICTIONARY METHOD 2        -> Builidng the dictionary on the go in runtime
# def twoSum4(nums, target):
#         dic={}
#         for i in range(len(nums)):
#              dic[nums[i]]=i
#              if target-nums[i] in dic and dic[target-nums[i]]!=i:
#                   return [i,dic[target-nums[i]]]
          
            
arr=[2,7,11,15]
x=9
print(twoSum1(arr,x))
print(twoSum2(arr,x))
print(twoSum3(arr,x))
# print(twoSum4(arr,x))

