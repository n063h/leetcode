#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start

def qpow(a,b):
    res=1
    while b>0:
        if b%2!=0:
            res*=a%1337
        a*=a%1337
        b//=2
    return res
        

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        bb=0
        for i in b:
            bb=bb*10+i
        return qpow(a,bb)%1337

# @lc code=end

