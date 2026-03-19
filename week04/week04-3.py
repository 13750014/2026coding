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
        return -1
