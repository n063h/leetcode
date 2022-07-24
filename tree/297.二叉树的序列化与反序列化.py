#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def deserialize(vals):
    if not vals:
        return None,vals
    val = vals[0]
    if val == '#':
        return None,vals[1:]
    l,vals = deserialize(vals[1:])
    r,vals = deserialize(vals)
    return TreeNode(val,l,r),vals

class Codec:

    def serialize(self, root):
        if not root:
            return '#'
        l,r=self.serialize(root.left),self.serialize(root.right)
        return f"{root.val} {l} {r}"
        
    def deserialize(self, data):
        vals=data.split(" ")
        root,_=deserialize(vals)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

