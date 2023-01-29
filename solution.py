class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        grid_not_empty = True
        while grid_not_empty:
            sub_arr_maxes = []
            for sub_arr in grid:
                max_num = 0
                max_index = 0
                for i in range(len(sub_arr)):
                    num = sub_arr[i]
                    if num > max_num:
                        max_num = num
                        max_index = i
                sub_arr_maxes.append(max_num)
                sub_arr.pop(max_index)
            total += max(sub_arr_maxes)
            if len(grid[0]) < 1:
                grid_not_empty = False
        return total
            

