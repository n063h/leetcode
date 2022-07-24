#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
res=None

def maxPathSum(root):
    if not root:
        return 0
    global res
    l,r=maxPathSum(root.left),maxPathSum(root.right)
    val=root.val
    cur=val+max(0,l,r,l+r)
    if not res:
        res=cur
    res=max(res,cur)
    return val+max(0,l,r)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global res
        res=None
        maxPathSum(root)
        return res
# @lc code=end

