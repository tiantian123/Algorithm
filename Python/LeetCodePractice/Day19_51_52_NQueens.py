#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/31 0:51
# @Author: Tian Chen
# @File: Day19_51_52_NQueens.py
"""
51. N-queens-I
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
52. N-queens-II
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.result = []
        self.col = set();
        self.pie = set()
        self.na = set()
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # recursion terminator
        if row >= n:
            self.result.append(cur_state)
            return

        for col in range(n):
            if col in self.col or row + col in self.pie or row - col in self.na:
                # go die
                continue
            # update the flags
            self.col.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            self.col.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i: i+n] for i in range(0, len(board), n)]


class Solution2:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p+q], xy_sum+[p-q])
        result = []
        DFS([], [], [])
        return [["."*i +"Q"+"."*(n-i-1) for i in col] for col in result]


