#week04-4a.py (重寫week04-2.py)
#LeetCode 1732. Find the Highest Altitude
#找到最高的海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 #一開始的高度是0
        for gg in gain: #python進階for迴圈:依序取出gg
            H +=gg
            ans = max(ans,H)
        return ans

        '''
# week04-2.py 學習計畫 prefix sun 第1題
#LeetCode 1732. Find the Highest Altitude
#找到最高的海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) #陣列的長度
        ans = H = 0 #一開始的高度是0
        #答案一開始是0，因為一開始的高度是0
        for i in range(N): #逐個加起來
            H += gain[i] #現在增減的量gain[i]加進H
            ans = max(ans, H) #更新最高的答案
        return ans'''
