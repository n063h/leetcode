#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxIndex(nums: List[int])->int:
    idx,m=0,nums[0]
    for i,num in enumerate(nums):
        if num>m:
            idx,m=i,num
    return idx,m
    
# 需要返回root，显然是后序遍历
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        idx,m=maxIndex(nums)
        node = TreeNode(m,self.constructMaximumBinaryTree(nums[:idx]),self.constructMaximumBinaryTree(nums[idx+1:]))
        return node
        
# @lc code=end

