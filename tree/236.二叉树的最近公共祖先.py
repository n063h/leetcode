#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
res=None
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    global res
    if res or not root:
        return res
    l,r=lowestCommonAncestor(root.left,p,q),lowestCommonAncestor(root.right,p,q)
    if res:
        return res
    s={p,q}
    a,b,c=l in s,r in s,root in s
    if (a and b) or (a and c) or (b and c):
        res=root
        return root
    if c:
        return root
    return l or r
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global res
        res=None
        return lowestCommonAncestor(root, p, q)
            
        
# @lc code=end

