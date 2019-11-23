# Solution for https://leetcode.com/problems/two-sum/
# Language : Python3

# O(n^2) Solution
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return i, j


