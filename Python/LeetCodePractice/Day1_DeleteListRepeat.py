#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/10 21:05
# @Author: Tian Chen
# @File: Day1_DeleteListRepeat.py

"""
26.删除有序数组中的重复值
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例：
给定数组 nums = [1,1,2], 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。你不需要考虑数组中超出新长度后面的元素。
"""
from typing import List

class Solution:
    """
    思路：使用前后双指针p和q, 当前后两个指针所指向的值相等时，前指针后移，当前后指针指向内容不相等时，将前指针的值赋值给后指针后移1位的结点
    优化：考虑到没有重复值时，拷贝数据消耗内存太大，加入判断语句 ，只有当 q - p > 1才进行拷贝
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        # 先判断数组是否为kong
        length = len(nums)
        if length == 0:
            return 0
        # 设置双指针
        p = 0
        q = 1
        while q < length:
            if nums[p] != nums[q]:
                if q - p > 1: # 减少数据转移的次数
                    nums[p + 1] = nums[q]
                p += 1
            q += 1

        return p + 1

if __name__ == "__main__":
    lst = [0,0,1,1,1,2,2,3,3,4]
    print("原始数组:", lst)
    test = Solution()
    length = test.removeDuplicates(lst)
    lst = lst[:length]
    print(f"移除重复值后的数组：", lst)
