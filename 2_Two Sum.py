#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
import sys
class Solution:
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for x in range(i+1,len(nums)):
                if nums[i]+nums[x]==target:
                    return i,x