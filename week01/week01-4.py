#week01-4.py 學習計畫 Array/String 第三題
#LeetCode 1431. Kids With the Greatest Number of Candies
#你給額外的extraCandies 後，小朋友手上的結果，會不會最多的?
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans =[] #答案的True 和False將塞在裡面
        best = max(candies) #目前小朋友「最多有幾個糖」
        for candie in candies: #逐一檢查，如果把extreCandies 給小朋友
            if candie+ extraCandies >= best:ans.append(True)
            else: ans.append(False) #他會不會 >=最多的，依序入座 ans
        return ans
