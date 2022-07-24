#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
import bisect
def lengthOfLIS1(nums):
    n=len(nums)
    dp=[1]*n
    for idx,num in enumerate(nums):
        k=1
        t=0
        for i in range(idx-1,-1,-1):
            if num>nums[i]:
                t=max(t,dp[i])
        dp[idx]=k+t
    return max(dp)
        
def lengthOfLIS2(nums): # 贪心+二分
    n=len(nums)
    stack=[] # 从小到大的子序列
    for idx,num in enumerate(nums):
        if not stack: 
            stack.append(num)
            continue
        i=bisect.bisect_right(stack, num)
        if num==stack[i-1]: # num已在栈中，无需修改
            continue
        if i>=len(stack): # num超过整个栈，可以构建更大的子序列
            stack.append(num)
        else: # num小于栈最大值(bisect_right结果不是len边界)，则将比它稍大的值替换，这样不会影响到已有序列，还可以将下一次构建子序列的门槛降低
            stack[i]=num
    return len(stack)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return lengthOfLIS2(nums)

# @lc code=end

"""
1. 动归保存以idx为结尾的最大子序列长度,需要向前看所有比它小的(能构建子序列)的dp
2. 贪心+二分,保存可能的子序列,每次拿到值替换比它稍大的数,以降低后续构建子序列的难度
"""