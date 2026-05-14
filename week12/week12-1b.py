#week12-1b.py 學習計畫 Graphs - DFS 第一題 Medium題
#LeetCode 841. Keys and Rooms
#房間裡有鑰匙，可以再開新的房間，最後能開全部房間嗎?
#DFS:Depth First Search 通常會利用stack或function stack(函式呼叫函式)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def helper(now): #函式呼叫函式的版本，也能進行DFS
            for k in rooms[now]:
                if k not in visited: #沒去過的房間
                    visited.add(k) #標記參觀中
                    helper(k) #就進去參觀
        visited.add(0) #標記參觀中
        helper(0) #一開始先參觀房間0
        return len(rooms) == len(visited)
