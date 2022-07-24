#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

res=[]
def pathSum(root,diff,path):
    global res
    if not root:
        return
    path.append(root.val)
    diff-=root.val
    if diff==0 and not (root.left or root.right):
        res.append([*path])
    if root.left:
        pathSum(root.left,diff,path)
    if root.right:
        pathSum(root.right,diff,path)
    path.pop()
    
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        global res
        res=[]
        pathSum(root, targetSum, [])
        return res
        
        
# @lc code=end

