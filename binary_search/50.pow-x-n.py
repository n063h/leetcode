#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        flag=1 if n>0 else -1
        n=abs(n)
        t=self.myPow(x, n//2)
        res=t*t if n%2==0 else t*t*x
        return 1/res if flag==-1 else res
# @lc code=end

