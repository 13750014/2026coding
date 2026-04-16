#week08-5.py 學習計畫 Binary Search 第三題
#LeetCode 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #笨方法：for迴圈不行嗎？
        N = len(nums) #陣列大小N
        if N==1: return 0 #i:0最大(只有1個數，就是最大，別再nums[i-1]nums[i+1]了拉)
        for i in range(N):
            if i==0: #沒有左邊，只測右邊(要比右邊大)
                if nums[i]> nums[i+1]: return i
            if i==N-1: #最右邊，沒有右邊，只測左邊(要比左邊大)
                if nums[i]> nums[i+1]: return i
            #下面會當機，因為i-1或i+1可能會超過範圍。所以加上面的if
            elif nums[i-1] < nums[i] and nums[i]>nums[i+1]:
                return i
