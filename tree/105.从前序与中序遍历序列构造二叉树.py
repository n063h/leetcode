#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not preorder:
            return None
        num=preorder[0]
        idx=inorder.index(num)
        l,r=self.buildTree(preorder[1:1+idx],inorder[:idx]),self.buildTree(preorder[1+idx:],inorder[idx+1:])
        return TreeNode(num,l,r)
# @lc code=end

