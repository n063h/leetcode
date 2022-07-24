#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start

def hIndex(citations): #[0,1,5,5,5,6]
    citations=[c for c in citations if c>0]
    if not citations:
        return 0
    l,r=0,len(citations)+1
    while l<r:
        mid=(l+r)//2
        low=len(citations)-mid
        if low<0:
            r=mid
            continue
        if citations[low]>=mid:
            l=mid+1
        else:
            r=mid
    return r-1

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return hIndex(citations)
# @lc code=end

"""
二分的取值范围[0,最大值+1)或者[0,len(citations)+1)都可以。
想求上界,向右收缩。
mid在这里是mid篇论文mid分,由多少篇论文可以从后往前推到第一篇该mid分的论文,检查是否满足即可。
"""