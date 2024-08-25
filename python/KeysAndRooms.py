# Runtime: 68ms
# Memory: 17.00MB

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_list = rooms[0]
        rooms[0] = [-1]

        while key_list:
            key = key_list.pop()
            if rooms[key] != [-1]:
                key_list += rooms[key]
            rooms[key] = [-1]
            
        return rooms.count([-1]) == len(rooms)
        
