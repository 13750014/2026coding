#week14-2c.py 學習計畫 DP - 1D 第一題 Easy
#LeetCode 1137. N-th Tribonacci Number
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        if n<3: return a[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
