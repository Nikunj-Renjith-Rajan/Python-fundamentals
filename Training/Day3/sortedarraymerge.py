# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
def merge(nums1, m, nums2, n):
        i=0
        j=0
        arr=[]
        while i<m and j<n:
            if(nums1[i]<nums2[j]):
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        if i==m:
            while(j<n):
                 arr.append(nums2[j])
                 j+=1
        elif j==n:
            while(i<m):
                 arr.append(nums1[i]) 
                 i+=1 
        return arr
                       
nums1=[3,5,7,8,9,12]
nums2=[2,4,8,10,11,15,16]
print(merge(nums1,len(nums1),nums2,len(nums2)))
