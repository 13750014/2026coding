#week02-5.py 學習計畫 Two Pointers 最後1題
#LeetCode 1679. Max Number of K-Sum Pairs
#希望找到「加起來==k」的pair 兩兩一組，共幾組
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() #小到大排好，等一下「左邊挑一個、右邊挑一個」看能不能組合
        ans = 0
        i, j = 0, len(nums) -1 #最左邊i對應最小，右邊j對應最大
        while i<j: #還沒有撞在一起，就可以左右個挑一個
            if nums[i] + nums[j] == k: #太好了剛剛好
                ans+=1
                i,j = i+1, j-1 #右邊用了，往右，右邊用了，往左
            if nums[i] + nums[j] < k: #加起來太小，那左邊小的i要往右移
                i+=1
            if nums[i] + nums[j] > k: #加起來太大，那右邊大的j要往左移
                j-=1
        return ans
