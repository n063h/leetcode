#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n=len(distance)
        if start>destination:
            start,destination = destination,start
        dp=[0]*n
        for idx,n in enumerate(distance):
            if idx==0:continue
            dp[idx]=dp[idx-1]+distance[idx-1]
        total,clock=dp[-1]+distance[-1],dp[destination]-dp[start]
        return min(clock,total-clock)
# @lc code=end

