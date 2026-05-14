#week12-1a.py 學習計畫 Graphs - DFS 第一題 Medium題
#LeetCode 841. Keys and Rooms
#房間裡有鑰匙，可以再開新的房間，最後能開全部房間嗎?
#DFS:Depth First Search 通常會利用stack或function stack(函式呼叫函式)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0] #我們利用stack裡面有待處理的房間，一開始房間0是開的
        visited = set() #有去過、處理過的房間，不要再進去
        visited.add(0) #已經排好了、等待處理，下次有拿到鑰匙，不要再放入stack
        while stack: #只要stack還有東西，就繼續處理
            now = stack.pop() #吐出1個房間裡，現在要來處理
            for k in rooms[now]: #把room now房間裡，所有的鑰匙k，都拿來檢查
                if k in visited: continue #鑰匙k對應的房間k看過了，別再檢查
                #如果走到這裡，代表沒走過、沒有待處理的房間
                stack.append(k) #加入stack資料結構
                visited.add(k) #標記這個房間也待處理、其他人不要再排處理
        return len(rooms) == len(visited) #房間的數目，全部都參觀過，成功
