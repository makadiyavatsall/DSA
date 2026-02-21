class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        take = True  

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            if i % 2 == 0:
                col_range = range(cols)          
            else:
                col_range = range(cols - 1, -1, -1)  

            for j in col_range:
                if take:
                    result.append(grid[i][j])
                take = not take   

        return result
        