#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l,r=0,n
        while l < r:
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid
            else:
                l=mid+1
        return l
        
# @lc code=end

