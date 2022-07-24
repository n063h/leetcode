#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 题意返回root，显然是后序遍历，自底而上
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        l,r=self.invertTree(root.left),self.invertTree(root.right)
        # 后序遍历,操作在后
        root.left,root.right=r,l
        return root
# @lc code=end

