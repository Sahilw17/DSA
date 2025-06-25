# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
nums=[1,2,3,4]
class Solution(object):
    def containsDuplicate(self, nums):
            h=set()
            for num in (nums):
                if num in h:
                    return True
                h.add(num)
            return False

        
m=Solution()

print(m.containsDuplicate(nums))