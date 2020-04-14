#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/14 20:15
# @Author: Tian Chen
# @File: 200_Islands_count.py
"""
200. Number of Islands

"""
import collections
from typing import List


class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        self.max_x, self.max_y = len(grid), len(grid[0])
        self.visited = set()
        self.grid = grid
        return sum([self.floodfill_BFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def _is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y <0 or y >= self.max_y:
           return False
        if self.grid[x][y] == '0' or (x, y) in self.visited:
           return False
        return True

    def floodfill_DFS(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.floodfill_DFS(x + self.dx[k], y + self.dy[k])
        return 1

    def floodfill_BFS(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        queue = collections.deque()
        queue.append((x, y))

        while queue:
            cur_x, cur_y = queue.popleft()
            for k in range(4):
                new_x, new_y = cur_x + self.dx[k], cur_y + self.dy[k]
                if self._is_valid(new_x, new_y):
                    self.visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return 1


class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n + j] = i*n + j
                    self.count += 1
        print('inital 1 count:', self.count)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def Union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rootx] = rooty
                self.rank[rooty] += 1
            self.count -= 1


class UnionSolution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        uf.Union(i*n + j, nr*n + nc)
        return uf.count



if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    result = Solution()
    count = result.numIslands(grid)
    print(count)
    res2 = UnionSolution()
    print(res2.numIslands(grid))