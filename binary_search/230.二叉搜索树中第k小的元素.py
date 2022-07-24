#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def kthSmallest(root,k):
    obj={'k':k}
    def traverse(root,obj):
        if not root:
            return None
        if obj['k']==0:
            return root.val
        t=traverse(root.left,obj)
        if t is not None:
            return t
        obj['k']-=1
        if obj['k']==0:
            return root.val
        return traverse(root.right,obj) 
    return traverse(root,obj)
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return kthSmallest(root, k)
        
# @lc code=end

"""
python里不能传&int减少k,可以传对象引用代理
"""