#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start

def searchInsert1(nums, target):
    l,r=0,len(nums)-1
    while l < r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return l if nums[l]>=target else l+1

def searchInsert2(nums, target):
    l,r=0,len(nums)
    while l < r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid
    return r

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return searchInsert2(nums, target)
# @lc code=end

"""
边界之外的,可以正常搜索,或者收缩,根据终止时的nums[l]和target的大小关系确定位置
"""