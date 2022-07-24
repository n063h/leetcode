#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q,res = [],[]
        if root:
            q.append(root)
        while q :
            layer=[]
            for _ in range(len(q)):
                node=q.pop(0)
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                layer.append(node.val)
            res.append(layer)
        return res
# @lc code=end

