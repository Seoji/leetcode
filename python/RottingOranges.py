#Runtime: 44ms
#Memory: 16.42MB

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_coords_list = []
        fresh_orange_cnt = 0
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if grid[row_idx][col_idx] == 2:
                    rotten_coords_list.append(tuple([row_idx, col_idx, 0]))
                if grid[row_idx][col_idx] == 1:
                    fresh_orange_cnt += 1

        rotten_coords_dq = deque(rotten_coords_list)
        mnt = 0
        while rotten_coords_dq:
            y_coord, x_coord, mnt = rotten_coords_dq.popleft()

            for new_y_coord, new_x_coord in [
                [y_coord+1, x_coord],
                [y_coord-1, x_coord],
                [y_coord, x_coord+1],
                [y_coord, x_coord-1]
            ]:
                if new_y_coord >= 0 and new_y_coord < len(grid) and \
                    new_x_coord >= 0 and new_x_coord < len(grid[0]) and \
                    grid[new_y_coord][new_x_coord] == 1:
                    grid[new_y_coord][new_x_coord] = 2
                    fresh_orange_cnt -= 1
                    rotten_coords_dq.append(tuple( [new_y_coord, new_x_coord] + [mnt+1] ))

        if fresh_orange_cnt > 0:
            return -1
        else:
            return mnt

