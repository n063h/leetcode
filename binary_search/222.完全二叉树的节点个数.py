#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def countNodes(root):
    def countLayers(root):
        if not root:
            return 0
        return countLayers(root.left)+1
    
    def exists(root,layer,target): # [1,2,3] 3
        # 1:1
        # 2:10         3:11  
        # 4:100  5:101  6:110  7:111
        if not root:
            return False
        layer-=1 # ignore root
        while layer>0:
            i=(1<<(layer-1))&target # find first num, which indicates direction
            layer-=1
            if i==0:
                root=root.left
            else:
                root=root.right
            if not root:
                return False
        return True
            
    layers=countLayers(root)
    if layers==0:
        return 0
    l,r=pow(2,layers-1),pow(2,layers)
    while l<r:
        mid=(l+r)//2
        if exists(root,layers,mid):
            l=mid+1
        else:
            r=mid
    return r-1

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return countNodes(root)
# @lc code=end

"""
完全二叉树节点序号有规律,但需要从1开始:l层序号abcd(l长度),a表示root,其后依次表示左右子树方向。
由于完全二叉树的性质,很容易由层数算得最后一层的序号上下界,再二分查找即可.二分是O(logn),查看是否存在一次是O(logn)即O(h),
所以总共是O((logn)^2)
"""