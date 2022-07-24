#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start

def findPeakElement(nums):
    l,r=0,len(nums)
    if r==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[-2]<nums[-1]:
        return r-1
    
    while l < r:
        mid=(l+r)//2
        v=nums[mid]
        if (mid==len(nums)-1 and nums[mid-1]<v) or ( nums[mid-1]<v and v>nums[mid+1]):
            return mid
        elif v<nums[mid-1]:
            r=mid
        else:
            l=mid+1
    return -1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return findPeakElement(nums)
# @lc code=end

"""
超升高的地方走
"""
