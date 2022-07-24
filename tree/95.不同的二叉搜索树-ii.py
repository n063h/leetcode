#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def generateTrees(vals):
    nodes = []
    if not vals:
        return [None]
    for idx,val in enumerate(vals):
        l,r=generateTrees(vals[:idx]),generateTrees(vals[idx+1:])
        for lnode in l:
            for rnode in r:
                node=TreeNode(val,lnode,rnode)
                nodes.append(node)
    return nodes

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        vals=[i+1 for i in range(n)]
        return generateTrees(vals)
        
# @lc code=end

