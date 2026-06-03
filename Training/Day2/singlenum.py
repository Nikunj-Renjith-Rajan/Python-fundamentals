# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

#METHOD 1   :   Using Dictionary  (Hashing)
def singleNum1(nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]==1:
                return i

#METHOD 2   :   Using XOR   :    Best time complexity
def singleNum2(nums):
        res=0
        for i in nums:
            res=res^i
        return res

#METHOD 3   :   Using Set
def singleNum3(nums):
        s1=set(nums)
        sum1=sum(nums)
        sum2=sum(s1)
        return ((sum2*2)-sum1)
    

arr=[2,1,4,1,2]
print(singleNum1(arr))
print(singleNum2(arr))
print(singleNum3(arr))