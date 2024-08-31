#Runtime: 686ms
#Memory: 16.97MB

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        result = 0
        dq = deque([tuple([entrance[0], entrance[1], 0])])

        while dq:
            y_coord, x_coord, mv_cnt = dq.popleft()
            
            if [y_coord, x_coord] != entrance and (
                y_coord in [0, len(maze) - 1] or 
                x_coord in [0, len(maze[0]) - 1]
            ):
                return mv_cnt

            for new_coords in [
                [y_coord+1, x_coord],
                [y_coord-1, x_coord],
                [y_coord, x_coord+1],
                [y_coord, x_coord-1]
            ]:
                if new_coords[0] < len(maze) and new_coords[0] >= 0 and \
                new_coords[1] < len(maze[0]) and new_coords[1] >= 0 and \
                maze[new_coords[0]][new_coords[1]] == '.':
                    maze[new_coords[0]][new_coords[1]] = '+'
                    dq.append(tuple(new_coords+[mv_cnt+1]))
        return -1

