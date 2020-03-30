#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/31 0:26
# @Author: Tian Chen
# @File: Day18_22_generate_parenthese.py
"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self._gen( 0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
        if left < n:
            self._gen(left + 1, right, n, result+"(")
        if left > right and right < n:
            self._gen(left, right + 1, n, result+")")


if __name__ == "__main__":
    n = 3
    res = Solution()
    print(res.generateParenthesis(n))