#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 关键是求得首尾，即子树min和max。
# min显然是子树根，故需要返回尾。
def flatten(root):
    if not root:
        return None
    l,r=flatten(root.left),flatten(root.right)
    # 左子树存在，则右接到左尾
    if l is not None:
        l.right=root.right
        root.right=root.left
    root.left = None
    # 尽量返回尾，r>l>root
    if r:return r
    if l:return l
    return root
    

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        flatten(root)
        
# @lc code=end

