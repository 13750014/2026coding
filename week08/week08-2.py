#week08-2.py 學習計畫 Binary Search Tree 第二題
#LeetCode 374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n:int)->int:
        """
        :type n: int
        :rtype: int
        """
        #方法1：寫神奇的bisect_left()寫法，只要一行
        return bisect_left(range(n+1), 0 ,key=lambda x:-guess(x))
        #for i in range(1, n+1): #「錯誤」暴力法，for迴圈找答案
        #    if guess(i) == 0: return i #猜中了答案是i
        #不能用上面的for迴圈，因為n有20億這麼大，試不完
        #要用小學「猜數字」每次範圍猜一半，比他大，比他小，縮小範圍
        #方法2：while left<right去逼近
        left, right = 1, n+1 #左右的範圍
        while left< right: #左右的範圍還沒有「撞在一起」
            mid = (left + right) // 2 #(猜)中間的數
            if guess(mid) == 0:return mid #猜到中間的數字
            if guess(mid)>0: left = mid +1 #(暗示你)在高一點(中點設成下界)
            else: right = mid #(暗示你)在低點(中點設成上界)
        return left
