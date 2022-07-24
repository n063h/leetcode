#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 不抢当前node，则左右独立都取最大的即可
def rob(root):
    if not root:
        return 0,0
    val = root.val
    l,not_l=rob(root.left)
    r,not_r=rob(root.right)
    rob_root=val+not_l+not_r
    not_rob_root=max(l,not_l)+max(r,not_r)
    return rob_root,not_rob_root

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(*rob(root))
        
# @lc code=end

