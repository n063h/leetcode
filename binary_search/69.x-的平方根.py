#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x+1
        while l < r:
            mid=(l+r)//2
            t=mid*mid
            if t==x:
                return mid
            elif t<x:
                l=mid+1
            else:
                r=mid
        return l-1 if l-1>=0 else 0 # l是比结果稍大一点点idx
# @lc code=end

