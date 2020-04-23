#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/14 0:07
# @Author: Tian Chen
# @File: 547_friend_circles.py
"""
547. Friend Circles
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we
defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith
and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend
circles among all the students.
Example:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
"""


class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.parent[i*n + j] = i *n + j
                    self.count += 1
        self.count -= m
        print('inital 1 count:', self.count)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]: return 0
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j  in range(n):
                if grid[i][j] == 0:
                    continue
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if 0 <= nr < m and 0<= nc < n and grid[nr][nc] == 1:
                        uf.union(i*n+j, nr*n+nc)
        return uf.count


if __name__ == "__main__":
    # grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    result = Solution()
    count = result.numIslands(grid)
    print(count)

