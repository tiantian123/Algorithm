#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/28 23:01
# @Author: Tian Chen
# @File: 51_Number_in_array.py
"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
示例：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
"""
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 先将所有值进行异或
        ret = 0
        for n in nums:
            ret ^= n
        div = 1
        while (div & ret) == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]