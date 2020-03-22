#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/22 17:52
# @Author: Tian Chen
# @File: Day9_Min_Incre_to_make_arr_uniq.py

"""
945. Minimum Increment to Make Array Unique
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
Return the least number of moves to make every value in A unique.
Example:
    1) Input: [1,2,2]
       Output: 1
       Explanation:  After 1 move, the array could be [1, 2, 3].
    2) Input: [3,2,1,2,1,7]
       Output: 6
       Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
       It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""
from typing import List


class Solution:
    def minIncrementForUnique1(self, A: List[int]) -> int:
        """
        sorted A
        """
        A.sort()
        move = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                move += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return move

    def minIncrementForUnique2(self, A: List[int]) -> int:
        level = -1
        res = 0
        for i in sorted(A):
            if level < i:
                level = i
            else:
                res += level - i + 1
                level += 1
        return res

if __name__ == "__main__":
    arr = [3,2,1,2,1,7]
    A = Solution()
    a1 = A.minIncrementForUnique2(arr)
    print(a1)