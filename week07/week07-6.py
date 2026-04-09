#week07-6.py 學習計畫 Queue 第2題
#LeetCode 649. Dota2 Senate 想知道3000的範圍內，有幾個ping
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0 #目前等待「被消滅的次數」都還是0
        R, D = senate.count('R'), senate.count('D') #字串裡數一數，目前各有幾個人
        while queue: #進行「互相Ban對方」的遊戲
            now = queue.popleft() #左邊吐出個字母，他要消滅「敵對陣營」
            if now=='R':
                if banR>0: #已經紀錄要消滅一個人
                    banR -= 1 #用掉一個消滅的名額
                    R -= 1 #馬上少掉一個人
                    continue #你一出現，就已經被消滅(換下一位)
                else: #你沒有被消滅，你可以反過來消滅對方
                    banD += 1
                    queue.append(now) #再到最右邊排隊
            else: #now =='D'
                if banD>0:
                    banD -= 1
                    D -= 1
                    #continue
                else:
                    banR += 1
                    queue.append(now)
            if R==0: return 'Dire' #把R消滅光，'D'就得勝
            if D==0: return 'Radiant' #把D消滅光，'R'就得勝
