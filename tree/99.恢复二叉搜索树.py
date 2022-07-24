#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 不要求返回root，考虑自顶向下
# 交换最顶和最底的错误点（恰好 两个节点的值被错误地交换）
# 故pair[0]只记一次（最顶），pair[1]持续更新更底部的值
pair,prev=[None,None],None
def recoverTree(root):
    if not root: 
        return
    recoverTree(root.left)
    global pair,prev
    if prev and root.val < prev.val:
        if not pair[0]:
            pair[0] = prev
        pair[1]=root
    prev=root
    recoverTree(root.right)

class Solution:
    def recoverTree(self, root) -> None:
        global pair,prev
        pair,prev=[None,None],None
        recoverTree(root)
        a,b = pair
        a.val,b.val = b.val,a.val
# @lc code=end

