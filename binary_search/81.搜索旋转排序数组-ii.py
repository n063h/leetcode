#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start

def search(nums, target):
    l,r=0,len(nums)
    while l < r:
        mid=(l+r)//2
        left,cur, right=nums[l],nums[mid],nums[r-1]
        if cur==target:
            return True
        if left==cur==right: # 无法判断，此时首位==cur!=target,可以删去
            l,r=l+1,r-1
        elif cur>right: # 可能在左边
            if left<=target<=cur:
                r=mid
            else:
                l=mid+1
        else:
            if cur<=target<=right:
                l=mid+1
            else:
                r=mid
    if l<len(nums) and nums[l]==target:
        return True
    return False
        
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return search( nums, target)
# @lc code=end

"""
注意r是开区间不能取到,所以r=mid,不能-1,否则多收缩了一位
"""