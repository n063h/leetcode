#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start

def multply(a,b):
    res=0
    while b>0:
        if (b&1)==1: # 奇数，右移要损失1，补上
            res+=a
        b>>=1
        a+=a
    return res

def divide(a,b):
    l,r=0,a # b整数，所以商最大是a
    while l<r:
        mid=(l+r)//2
        v=multply(b,mid)
        if v<=a and v+b>a:
            return mid
        elif v>a:
            r=mid
        else:
            l=mid+1
    return l

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a,b=dividend,divisor
        res=divide(abs(a),abs(b))
        if a*b<0:
            res*=-1
        if res>= pow(2, 31):
            return pow(2, 31)-1
        return res
# @lc code=end

"""
官方：快速幂+二分
我的第一反应是快速幂加上去,一旦再加aa就爆了,就让aa重新从a快速幂加上去。应该可以用memo和降序+aa的方式优化。
"""
