# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution():
    def merge(self, nums1, m, nums2, n):
      # nums1=[x  for x in nums1 if x!=0]
      # nums2=[x for x in nums2 if x!=0 ]
      # nums1=nums1[0:m]
      # nums2=nums2[0:n]
      for i in range(n):
         nums1[m+i]=nums2[i]
      
      temp=0
      l=len(nums1)

      for i in range (0,l):
        for j in range (1,l-1-i):
           if(nums1[j]>nums1[j+1]):
              temp=nums1[j]
              nums1[j]=nums1[j+1]
              nums1[j+1]=temp
      return nums1 
    
m=Solution()
l1=[2,0]
c=1
l2=[1]
n=1
print(m.merge(l1,c,l2,n))

           
           


