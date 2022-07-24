#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start

def findMin(nums):
    l,r=0,len(nums)
    while l < r:
        mid=(l+r)//2
        left,cur,right=nums[l],nums[mid],nums[r-1]
        if r<len(nums): # 本来右是开区间，取不到的，但为了让“左边或右边”r-=1后cur>right正确判定，还是让取到了
            right=nums[r]
        if left == cur==right and r-l>1:
            l,r=l+1,r-1
        if left < cur<right:
            r=mid
            continue
        if cur>right: # 左边 
            l=mid+1
        elif cur==right: # 左边或右边
            r=r-1
        else: # 右边
            r=mid
    return nums[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return findMin(nums)
# @lc code=end