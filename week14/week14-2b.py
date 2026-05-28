#week14-2b.py 學習計畫 DP - 1D 第一題 Easy
#LeetCode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        @cache
        def helper(i):
            if i<3: return a[i]
            return helper(i-1) + helper(i-2) + helper(i-3)
        return helper(n)

        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
