#week05-3.py 厩策璸礶 Hash Table (Map/Set)
#LeetCode 1207. Unique Number of Occurrences
#–贺计瞷Ω计ゲ斗常ぃ妓
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) #参璸计瞷Ω计\
        s = set() #ノㄓ瞷Ω计琌縒礚
        for c in counter: #盢计硋ㄓ
            #print(c, counter[c]) #计瞷碭Ω
            #counter[c]琌縒礚
            if counter[c] in s:
                return False
            s.add(counter[c]) #瞷硂瞷Ω计s柑
        return True #繦獽return
