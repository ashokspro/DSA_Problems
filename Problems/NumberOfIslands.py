class Solution:
    def makezero(self, grid, i, j):
        r = len(grid)
        c = len(grid[0])
        if i < 0 or j < 0 or i >= r or j >= c:
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.makezero(grid, i+1,j)
        self.makezero(grid ,i,j+1)
        self.makezero(grid ,i-1,j)
        self.makezero(grid ,i,j-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    self.makezero(grid, i, j)

        return count
