#week04-4c.py (重寫week04-4b.py)
#Leetcode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = Counter(nums) #使用資料結構，可以統計數量
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1: return nn
        return -1
'''
#weeK04-4b.py (重寫week04-3.py)
#Leetcode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0]*200
        for nn in nums: #把陣列的值，逐一取出來
            H[nn] += 1 #統計數量
        for nn in nums: #再來一次，逐一取出來
            if nn % 2 == 0 and H[nn] == 1: return nn #偶數and落單
        return -1

#week04-3.py More Challenges 的簡單題
#LeetCode 3866. First Unique Even Element
#找到陣列nums裡「只出現過1次的偶數」是誰
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans = -1 #找不到答案，會是-1
        N=len(nums) #有N個數
        H = [0]*200 #很多格，H[]對應 出現幾次
        for i in range (N):
            H[nums[i]] += 1 #把出現的數字，塞進H[??]裡
        #再逐個檢查「偶數」出現幾次
        for i in range(N): #逐一檢查
            if nums[i] % 2 == 0 and H[nums[i]] == 1: #偶數，只出現一次
                return nums[i] #找到答案
        return -1'''
