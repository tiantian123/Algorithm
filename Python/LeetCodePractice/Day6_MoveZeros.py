#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/15 21:35
# @Author: Tian Chen
# @File: Day6_MoveZeros.py
"""
283. Move zeros
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
"""
from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """

        """
        j = 0  # 记录非0 元素
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1