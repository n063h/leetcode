#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start

def findMin2(nums):
    l,r=0,len(nums)
    while l < r:
        mid=(l+r)//2
        left,cur,right=nums[l],nums[mid],nums[r-1]
        if left == cur==right and r-l>1:
            l,r=l+1,r-1
            continue
        if left < cur<right:
            r=mid
            continue
        if cur>right: # 左边
            l=mid+1
        else: # 右边
            if mid==0 or nums[mid-1]>cur:
                return cur
            else:
                r=mid
    return nums[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return findMin2(nums)
# @lc code=end

