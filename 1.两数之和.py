#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for idx,num in enumerate(nums):
            if (n:=target-num) in m:
                return [m[n],idx]
            m[num]=idx
        return []
# @lc code=end

