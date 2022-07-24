#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

m=dict()
res=[]

def findDuplicateSubtrees(root):
    global m,res
    if not root:
        return "#"
    l,r=findDuplicateSubtrees(root.left),findDuplicateSubtrees(root.right)
    s=f"{root.val} {l} {r}"
    if s not in m:
        m[s]=1
    else:
        if m[s]==1:
            res.append(root)
        m[s]+=1
    return s
        

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        global res,m
        res,m=[],dict()
        findDuplicateSubtrees(root)
        return res
# @lc code=end

