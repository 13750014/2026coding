#week14-3a.py 學習計畫 DP - 1D 第2題 Easy
#LeetCode 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache #函式呼叫函式，，把大問題，猜成小問題
        def helper(i): #現在踩在第i格，之後要多少錢
            if i >= len(cost):return 0 #終止條件
            return  cost[i] + min(helper(i+1), helper(i+2)) #函式呼叫函式
        return min(helper(0), helper(1)) #函式呼叫函式
