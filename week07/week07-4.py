#week07-4.py 學習計畫 Stack 最後1題
#LeetCode 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] #利用stack處理「方括號」及對應的「數字」
        nowN, nowS = 0, '' #左邊nowN數字 vs. 右邊nowS字串
        for c in s:
            if c.isdigit(): #若是數字 就用十進位組合起來
                nowN = nowN*10+int(c)
            elif c.isalpha(): #如果是字母 就讓「字串」變長
                nowS += c
            elif c=='[': #上括號：「數字」「字串」放入stack
                stack.append((nowN, nowS))
                nowN, nowS = 0, '' #一組新的「數字」「字串」
            elif c==']': #下括號：取出「數字」「字串」
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS #重複的次數 * 字串
        return nowS
