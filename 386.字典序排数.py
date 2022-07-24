#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

# @lc code=start


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s,res=[0],[]
        while s:
            num=s.pop()
            for i in range(9,-1,-1):
                t=num*10+i
                if 0<t<=n:
                    s.append(t)
            res.append(num)
        return res[1:]
            
# @lc code=end

