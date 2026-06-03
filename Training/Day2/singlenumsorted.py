#Given a sorted array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def singleNum(arr):
        for i in range(0,len(arr),2):
            if i==len(arr)-2 and arr[i]!=arr[i+1]:
                return arr[i]
        return arr[i]
arr=[1,1,2,2,4]
print(singleNum(arr))