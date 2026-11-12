class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        count = 0
        visited = set()
        for row, _ in enumerate(grid):
            for col, __ in enumerate(_):
                if grid[row][col] == "1" and (row,col) not in visited:
                    count+=1
                    q.append((row,col))
                    self.bfsIslands(visited, grid, (row,col), q)
        return count

    def bfsIslands(self, visited: set(tuple(int)), grid: List[List[str]], land: tuple(int), q: deque):
        mheight = len(grid)
        mwidth = len(grid[0])

        #we know land is valid
        h, w = land[0], land[1]
        visited.add((h,w))
        
        while q:
            if self.valNum(h-1, w, mheight, mwidth) and ((h-1, w) not in visited) and grid[h-1][w] ==  "1":
                q.append((h-1,w))
            if self.valNum(h+1, w, mheight, mwidth) and ((h+1, w) not in visited) and grid[h+1][w] ==  "1":
                q.append((h+1,w))
            if self.valNum(h, w-1, mheight, mwidth) and ((h, w-1) not in visited) and grid[h][w-1] ==  "1":
                q.append((h,w-1))
            if self.valNum(h, w+1, mheight, mwidth) and ((h, w+1) not in visited) and grid[h][w+1] ==  "1":
                q.append((h,w+1))
            self.bfsIslands(visited, grid, q.pop(), q)

    def valNum(self, height: int, width: int, max_h: int, max_w: int) -> bool:
        if height < 0 or height >= max_h or width < 0 or width >= max_w:
            return False
        return True

        